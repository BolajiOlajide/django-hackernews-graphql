from graphene import ObjectType, Mutation, List, Int, String
from graphene_django import DjangoObjectType

from .models import Link


class LinkType(DjangoObjectType):
    class Meta:
        model = Link


class Query(ObjectType):
    links = List(LinkType)

    def resolve_links(self, info, **kwargs):
        return Link.objects.all()


class CreateLink(Mutation):
    id = Int()
    url = String()
    description = String()

    class Arguments:
        url = String()
        description = String()

    def mutate(self, info, url, description):
        link = Link(url=url, description=description)
        link.save()

        return CreateLink(
            id=link.id,
            url=link.url,
            description=link.description,
        )


class Mutation(ObjectType):
    create_link = CreateLink.Field()
