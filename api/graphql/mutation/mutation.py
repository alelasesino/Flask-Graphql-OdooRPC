from graphene import ObjectType
from api.odoorpc.farm_resolvers import CreateFarm, RemoveFarm

class Mutation(ObjectType):
    createFarm = CreateFarm.Field()
    removeFarm = RemoveFarm.Field()