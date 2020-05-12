from graphene import Field, String, Int 
from api.odoorpc.utils import get_model
from api.graphql.query.query_types import Product
import datetime


def resolve_products(self, info):

    products = []
    product_model = get_model('product.product') 
    product_ids = product_model.search([])

    for product in product_model.browse(product_ids):

        product = Product(
            id=product.id,
            display_name=product.display_name,
            code=product.code,
            barcode= "" if not product.barcode else product.barcode,
            categ_id=product.categ_id.id
        )

        products.append(product)

    return products

