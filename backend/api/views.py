from api.models import Proposal, Product, Client, Response
from users.models import User
from api.serializers import ProposalSerializer, UserSerializer, ResponseSerializer, ProductSerializer, ClientSerializer

from rest_framework import viewsets
from rest_framework import permissions


class ProposalViewSet(viewsets.ModelViewSet):
    """
    `list`, `create`, `retrieve`, `update` and `destroy` actions for
    the Proposal model.
    """
    serializer_class = ProposalSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    model = Proposal

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        """ Filter to only the proposals by the logged in user """
        user = self.request.user
        if user.is_staff:
            return Proposal.objects.all()
        return Proposal.objects.filter(user=user)

class ResponseViewSet(viewsets.ModelViewSet):
    """
    `list`, `create`, `retrieve`, `update` and `destroy` actions for
    the Response model.
    """
    serializer_class = ResponseSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    model = Response

    def get_queryset(self):
        """ Filter to only the responses by the logged in user """
        user = self.request.user
        if user.is_staff:
            return Response.objects.all()
        return Response.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserViewSet(viewsets.ModelViewSet):
    """
    `list`, `create`, `retrieve`, `update` and `destroy` actions for
    the User model.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ClientViewSet(viewsets.ModelViewSet):
    """
    `list`, `create`, `retrieve`, `update` and `destroy` actions for
    the Client model.
    """
    serializer_class = ClientSerializer
    model = Client

    def get_queryset(self):
        """ Filter to only the clients created by the logged in user """
        user = self.request.user
        if user.is_staff:
            return Client.objects.all()
        return Client.objects.filter(user=user)



class ProductViewSet(viewsets.ModelViewSet):
    """
    `list`, `create`, `retrieve`, `update` and `destroy` actions for
    the Product model.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
