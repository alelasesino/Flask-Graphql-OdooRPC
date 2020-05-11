from graphene import Mutation, Field, String, InputObjectType, Interface, Int, Union
from api.odoorpc.utils import get_model
from api.graphql.query.query_types import Farm
from api.odoorpc.utils import farm_to_object, parcel_to_object
from api.graphql.mutation.input_types import InputFarm
from api.odoorpc import odoo

def resolve_farm(self, info, id):

    farm_model = get_model('agro.farm') 
    farm = farm_model.browse(id)
    return farm_to_object(farm)


def resolve_farms(self, info):

    farms = []
    farm_model = get_model('agro.farm') 
    farm_ids = farm_model.search([])

    for farm in farm_model.browse(farm_ids):
        farms.append(farm_to_object(farm))
    return farms


class CreateFarm(Mutation):

    class Arguments:
        farm = InputFarm(required=True)

    Output = Farm

    def mutate(self, info, farm):
        farm_model = get_model('agro.farm')

        if 'parcels' in farm:
            parcel_ids = []
            for parcel in farm['parcels']:
                parcel_ids.append((0, 0, parcel))
            farm['parcel_ids'] = parcel_ids
            farm.pop('parcels')

        id = farm_model.create(farm)
        new_farm = farm_model.browse(id)
        return farm_to_object(new_farm)


class RemoveFarm(Mutation):

    class Arguments:
        id = Int(required=True)

    Output = Farm

    def mutate(self, info, id):
        farm_model = get_model('agro.farm')
        delete_farm = farm_model.browse(id)
        removed_farm = farm_to_object(delete_farm)
        odoo.execute('agro.farm', 'unlink', [id])
        return removed_farm