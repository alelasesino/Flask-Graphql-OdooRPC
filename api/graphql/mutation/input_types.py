from graphene import InputObjectType, Int, String, DateTime, List


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