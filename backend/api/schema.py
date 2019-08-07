import graphene

from graphene_django.types import DjangoObjectType

from api.models import MyModel
from users.models import User


class MyModelType(DjangoObjectType):
    class Meta:
        model = MyModel

    # Add properties as fields
    some_property = graphene.Int()


class UserType(DjangoObjectType):
    class Meta:
        model = User


class Query(object):
    all_mymodels = graphene.List(MyModelType)
    all_users = graphene.List(UserType)
    mymodel = graphene.Field(MyModelType, id=graphene.Int())
    user = graphene.Field(UserType, id=graphene.Int(), email=graphene.String())

    def resolve_all_users(self, info, **kwargs):
        return User.objects.all()

    def resolve_user(self, info, **kwargs):
        id = kwargs.get('id')
        email = kwargs.get('email')

        if id is not None:
            return User.objects.get(pk=id)

        if email is not None:
            return User.objects.get(email=email)

        return None

    def resolve_all_mymodels(self, info, **kwargs):
        return MyModel.objects.select_related('user').all()

    def resolve_mymodel(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return MyModel.objects.get(pk=id)

        return None
