from graphene import Schema
from api.graphql.types import Product
from api.graphql.query import Query
from flask_graphql import GraphQLView
from api import app

schema = Schema(query=Query, types=[Product])

app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

# Optional, for adding batch query support (used in Apollo-Client)
#app.add_url_rule('/graphql/batch', view_func=GraphQLView.as_view('graphql', schema=schema, batch=True))


