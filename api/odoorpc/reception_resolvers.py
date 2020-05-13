from graphene import Field, String, Int, Mutation
from api.odoorpc.utils import get_model, get_model_by_id, utc_to_local
from api.graphql.query.query_types import Reception, ProductReception
from api.graphql.mutation.input_types import InputReception, InputProduct
import datetime


def resolve_reception(self, info, id):

    Picking = get_model('stock.picking') 
    reception_id = Picking.search([('id', '=', id)])

    picking = Picking.browse(reception_id)
    scheduled_date=utc_to_local(picking.scheduled_date)

    reception = Reception(
        id=picking.id,
        display_name=picking.display_name,
        scheduled_date=scheduled_date,
        receive_from=picking.location_id.id,
        time=scheduled_date.strftime("%H:%M")
    )

    receive_products = []

    for backorder in picking.move_ids_without_package:
        
        for f in backorder.move_line_nosuggest_ids:
            
            product = f.product_id

            receive_product = ProductReception(
                id=product.id,
                display_name=product.display_name,
                kilos=f.qty_done,
                lote=f.lot_id.name
            )

            receive_products.append(receive_product)

    reception.receive_products = receive_products

    return reception


def resolve_receptions(self, info, today):

    receptions = []
    Picking = get_model('stock.picking') 
    reception_ids = Picking.search([('location_id.id', '=', 83)])  #FILTRO POR FINCA

    for picking in Picking.browse(reception_ids):

        scheduled_date=utc_to_local(picking.scheduled_date)

        if datetime.datetime.today().day == scheduled_date.day or not today:

            reception = Reception(
                id=picking.id,
                display_name=picking.display_name,
                scheduled_date=scheduled_date,
                receive_from=picking.location_id.id,
                time=scheduled_date.strftime("%H:%M")
            )

            receive_products = []

            for backorder in picking.move_ids_without_package:
                
                for f in backorder.move_line_nosuggest_ids:
                    
                    product = f.product_id

                    #if f.lot_name == '225':
                    #kilos=get_kilos(product.product_template_attribute_value_ids[0].name, f.qty_done

                    receive_product = ProductReception(
                        id=product.id,
                        display_name=product.display_name,
                        kilos=f.qty_done,
                        lote=f.lot_id.name
                    )

                    receive_products.append(receive_product)

            reception.receive_products = receive_products
            receptions.append(reception)

    return receptions


def get_partner_location_id(farm_id):
    farm_model = get_model('agro.farm')
    farm = farm_model.browse(farm_id)
    return (farm.partner_id.id, farm.partner_id.property_stock_supplier.id)


def get_or_create_lot(product_id, lot):
    lot_model = get_model('stock.production.lot')
    lot_id = lot_model.search([('name', '=', lot), ('product_id.id', '=', product_id)])

    if len(lot_id) > 0:
        return lot_model.browse(lot_id).id
    else:
        return (0, 0, {
            'company_id': 1,
            'name': lot,
            'product_id': product_id
        })


def get_stock_move_line(date, location, product, quantity, lot):

    line = (0, 0, {
                    'company_id': 1,
                    'date': date,
                    'location_dest_id': 8, 
                    'location_id': location,
                    'product_uom_id': product.uom_id.id,
                    # 'product_uom_qty': quantity,
                    'qty_done': quantity,
                    'product_id': product.id,
                    'lot_id': get_or_create_lot(product.id, lot),
                    'state': 'assigned'
                    })

    return line


def get_stock_move(date, location, product_id, quantity, lot):

    product = get_model_by_id('product.product', product_id)
    print("DATE: ", date)
    move = (0, 0, {
                    'company_id': 1, 
                    'date': date, 
                    'date_expected': date, 
                    'location_dest_id': 8, 
                    'location_id': location, 
                    'name': product.display_name,
                    'product_id': product_id,
                    'product_uom': product.uom_id.id,
                    'needs_lots': 'lot' in product.tracking,
                    'description_picking': product.name,
                    'picking_code': 'incoming',
                    'state': 'assigned',
                    'move_line_nosuggest_ids': [get_stock_move_line(date, location, product, quantity, lot)]
                })

    return move


class CreateReception(Mutation):

    class Arguments:
        reception = InputReception(required=True)

    Output = Reception

    def mutate(self, info, reception):

        picking_model = get_model('stock.picking') 

        partner_location = get_partner_location_id(reception["farm_id"])

        partner_id = partner_location[0]
        location_id = partner_location[1]

        today =  datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

        move_ids_without_package = []

        for product in reception["products"]:
            move = get_stock_move(today, location_id, product["id"], product["quantity"], product["lot"])
            move_ids_without_package.append(move)

        picking_dict = {   #STOCK.PICKING
            'location_dest_id': 8, #WH/Stock
            'location_id': location_id, #Finca #1
            'picking_type_id': 1, #Entrega
            'partner_id': partner_id, #Finca #1
            'immediate_transfer': True,
            'priority': 0,
            'move_ids_without_package': move_ids_without_package
            }
        
        new_picking = picking_model.create(picking_dict)

        pick = picking_model.browse(new_picking)

        for package in pick.move_ids_without_package:
            for nosuggest in package.move_line_nosuggest_ids:
                nosuggest.write({'picking_id': new_picking})

        return resolve_reception(self, info, new_picking)


