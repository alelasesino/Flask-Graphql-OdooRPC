from api.odoorpc.utils import get_model
from api.odoorpc.utils import farm_to_object, parcel_to_object


def resolve_parcel(self, info, id):

    parcel_model = get_model('agro.farm.parcel') 
    parcel = parcel_model.browse(id)

    return parcel_to_object(parcel)


def resolve_parcels(self, info):

    parcels = []
    parcel_model = get_model('agro.farm.parcel') 
    parcel_ids = parcel_model.search([])

    for parcel in parcel_model.browse(parcel_ids):
        parcels.append(parcel_to_object(parcel))
    
    return parcels


