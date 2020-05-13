from graphene import InputObjectType, Int, String, DateTime, List, Float


class InputParcel(InputObjectType):
    name = String()
    number = Int()
    description = String()


class InputFarm(InputObjectType):
    name = String()
    description = String()
    code = String()
    partner_id = Int()
    parcels = List(InputParcel)


class InputProduct(InputObjectType):
    id = Int()
    lot = String()
    quantity = Float()


class InputReception(InputObjectType):
    farm_id = Int()
    products = List(InputProduct)
