from django.contrib.auth import get_user_model
from graphene import Mutation, Field, String, ObjectType, List
from graphene_django import DjangoObjectType


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()


class Query(ObjectType):
    users = List(UserType)

    def resolve_users(self, info):
        return get_user_model().objects.all()


class CreateUser(Mutation):
    user = Field(UserType)

    class Arguments:
        username = String(required=True)
        password = String(required=True)
        email = String(required=True)

    def mutate(self, info, username, password, email):
        user = get_user_model()(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()

        return CreateUser(user=user)


class Mutation(ObjectType):
    create_user = CreateUser.Field()
