from api.models import MyModel
from users.models import User
from api.serializers import MyModelSerializer, UserSerializer

from rest_framework import viewsets
from rest_framework import permissions

class MyModelViewSet(viewsets.ModelViewSet):
    """
    `list`, `create`, `retrieve`, `update` and `destroy` actions for
    the MyModel model.
    """
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserViewSet(viewsets.ModelViewSet):
    """
    `list`, `create`, `retrieve`, `update` and `destroy` actions for
    the User model.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
