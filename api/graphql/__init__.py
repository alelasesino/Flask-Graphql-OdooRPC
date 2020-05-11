from graphene import Schema
from api.graphql.query.query import Query
from api.graphql.mutation.mutation import Mutation
from flask_graphql import GraphQLView
from api import app

schema = Schema(query=Query, mutation=Mutation, auto_camelcase=False)

app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

# Optional, for adding batch query support (used in Apollo-Client)
#app.add_url_rule('/graphql/batch', view_func=GraphQLView.as_view('graphql', schema=schema, batch=True))


