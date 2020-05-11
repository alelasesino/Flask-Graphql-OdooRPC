from api.odoorpc import odoo
from api.graphql.query.query_types import Farm, Parcel

def get_model(name):
    if name in odoo.env:
        return odoo.env[name]
    else:
        raise ValueError('Odoo model not exist!.')


def farm_to_object(recorset):

    parcels = []
    for parcel in recorset.parcel_ids:
        parcels.append(parcel_to_object(parcel))

    return Farm(
        id=recorset.id,
        name=recorset.name,
        create_date=recorset.create_date,
        description=recorset.description,
        code=recorset.code,
        parcels=parcels
    )


def parcel_to_object(recorset):
    return Parcel(
        id=recorset.id,
        name=recorset.name,
        create_date=recorset.create_date,
        number=recorset.number,
        description=recorset.description
    )
