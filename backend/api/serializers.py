from rest_framework import serializers
from api.models import MyModel
from users.models import User


class MyModelSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = MyModel
        fields = ('id', 'user', 'created', 'modified', 'field_1', 'field_2', 'field_3', 'some_property')


class UserSerializer(serializers.ModelSerializer):
    related_name_set = MyModelSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'date_joined', 'related_name_set')
