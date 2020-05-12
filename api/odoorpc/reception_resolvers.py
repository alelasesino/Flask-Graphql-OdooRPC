from graphene import Field, String, Int 
from api.odoorpc.utils import get_model, utc_to_local
from api.graphql.query.query_types import Reception, ProductReception
import datetime

def resolve_reception(self, info, id):
    pass


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




# class CreateReception(Mutation):

#     class Arguments:
#         farm = InputFarm(required=True)

#     Output = Farm

#     def mutate(self, info, farm):
#         farm_model = get_model('agro.farm')

#         if 'parcels' in farm:
#             parcel_ids = []
#             for parcel in farm['parcels']:
#                 parcel_ids.append((0, 0, parcel))
#             farm['parcel_ids'] = parcel_ids
#             farm.pop('parcels')

#         id = farm_model.create(farm)
#         new_farm = farm_model.browse(id)
#         return farm_to_object(new_farm)
