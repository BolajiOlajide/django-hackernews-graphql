from graphene import ObjectType, Schema
import graphql_jwt

import links.schema
import links.schema_relay
import hackernews.users.schema


class Query(
            hackernews.users.schema.Query,
            links.schema.Query,
            links.schema_relay.RelayQuery,
            ObjectType):
    pass


class Mutation(
                links.schema_relay.RelayMutation,
                hackernews.users.schema.Mutation,
                links.schema.Mutation, ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = Schema(query=Query, mutation=Mutation)
