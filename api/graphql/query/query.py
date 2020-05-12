from graphene import ObjectType, Field, List, Int, Boolean
from api.graphql.query.query_types import Farm, Parcel, Reception, ProductReception, Product
from api.odoorpc.farm_resolvers import resolve_farm, resolve_farms
from api.odoorpc.parcel_resolvers import resolve_parcel, resolve_parcels
from api.odoorpc.reception_resolvers import resolve_receptions
from api.odoorpc.product_resolvers import resolve_products

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

    receptions = List(Reception, today=Boolean())

    def resolve_receptions(self, info, today):
        return resolve_receptions(self, info, today)

    products = List(Product)

    def resolve_products(self, info):
        return resolve_products(self, info)
