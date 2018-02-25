from rest_framework import serializers
from .models import product
from django.contrib.auth.models import User


class salesSerializers(serializers.ModelSerializer):

    class Meta:
        model = product
        fields = ['pk'  , 'name' , 'price' ,'quantity' , 'pos']

class UserSerializer(serializers.ModelSerializer):
    """A user serializer to aid in authentication and authorization."""

    itemslist = serializers.PrimaryKeyRelatedField(many=True, queryset=product.objects.all())
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        """Map this serializer to the default django user model."""
        model = User
        fields = ('id', 'username','itemslist' , 'user')
