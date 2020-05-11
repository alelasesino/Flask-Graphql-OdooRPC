from graphene import ObjectType, Field, List, Int
from api.graphql.query.query_types import Farm, Parcel
from api.odoorpc.farm_resolvers import resolve_farm, resolve_farms
from api.odoorpc.parcel_resolvers import resolve_parcel, resolve_parcels

class Query(ObjectType):

    farms = List(Farm)
    farm = Field(Farm, id=Int(required=True))

    def resolve_farm(self, info, id):
        return resolve_farm(self, info, id)

    def resolve_farms(self, info):
        return resolve_farms(self, info)

    parcels = List(Parcel)
    parcel = Field(Parcel, id=Int(required=True))

    def resolve_parcel(self, info, id):
        return resolve_parcel(self, info, id)

    def resolve_parcels(self, info):
        return resolve_parcels(self, info)

