import graphene

from api.schema import Query as APIQuery


class Query(APIQuery, graphene.ObjectType):
    # This class will inherit from multiple Queries
    pass


schema = graphene.Schema(query=Query)
