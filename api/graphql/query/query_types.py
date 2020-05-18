from graphene import ObjectType, String, Int, DateTime, List, Float


class Parcel(ObjectType):
    id = Int()
    name = String()
    create_date = DateTime()
    number = Int()
    description = String()


class Farm(ObjectType):
    id = Int()
    name = String()
    create_date = DateTime()
    description = String()
    code = String()
    partner_id = Int()
    parcels = List(Parcel)


class ProductReception(ObjectType):
    id = Int()
    display_name = String()
    kilos = Float()
    lote = String()


class Reception(ObjectType):
    id = Int()
    display_name = String()
    scheduled_date = DateTime()
    receive_from = Int()
    time = String()
    receive_products = List(ProductReception)


class Product(ObjectType):
    id = Int()
    display_name = String()
    code = String()
    barcode = String()
    categ_id = Int()
    image = String()










