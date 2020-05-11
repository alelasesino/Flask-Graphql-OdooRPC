from graphene import ObjectType, String, Int, DateTime, List


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
    parcels = List(Parcel)







