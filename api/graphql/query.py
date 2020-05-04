from graphene import ObjectType, Field, List, NonNull, Int
from api.graphql.types import Product

from api.odoorpc import odoo

class Query(ObjectType):

    products = List(NonNull(Product))
    product = Field(Product, id=Int(required=True))

    def resolve_product(self, info, id):
        return Product()


    def resolve_products(self, info):

        products = []

        if 'agro.farm' in odoo.env:
            Farm = odoo.env['agro.farm']
            farm_ids = Farm.search([])
            for farm in Farm.browse(farm_ids):
                product = Product()
                product.id = farm.id
                product.name = farm.description
                products.append(product)
        
        return products

