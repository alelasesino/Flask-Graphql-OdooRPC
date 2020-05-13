from graphene import ObjectType
from api.odoorpc.farm_resolvers import CreateFarm, RemoveFarm
from api.odoorpc.reception_resolvers import CreateReception

class Mutation(ObjectType):
    createFarm = CreateFarm.Field()
    removeFarm = RemoveFarm.Field()

    createReception = CreateReception.Field()