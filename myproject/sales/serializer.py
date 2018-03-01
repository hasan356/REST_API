from rest_framework import serializers
from .models import product
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator

User = get_user_model()


class salesListSerializers(serializers.ModelSerializer):


    class Meta:
        model = product
        fields = [ 'name' , 'price' ,'quantity' , 'pos']




class salesDetailSerializers(serializers.ModelSerializer):

    user = serializers.SerializerMethodField()
    class Meta:
        model = product
        fields = ['pk'  ,'user'  , 'name' , 'price' ,'quantity' , 'pos']

    def get_user(self , obj):
        return str(obj.user.username)




# class UserSerializer(serializers.ModelSerializer):
#     """A user serializer to aid in authentication and authorization."""
#
#     # itemslist = serializers.PrimaryKeyRelatedField(many=True, queryset=product.objects.all())
#     user = serializers.ReadOnlyField(source='user.username')
#
#     class Meta:
#         """Map this serializer to the default django user model."""
#         model = User
#         fields = ('id', 'user',)
#
#
# class UserRegisterSerializer(serializers.ModelSerializer):
#     email = serializers.EmailField(
#         required=True,
#         validators=[UniqueValidator(queryset=User.objects.all())]
#     )
#     username = serializers.CharField(
#         validators=[UniqueValidator(queryset=User.objects.all())]
#     )
#     password = serializers.CharField(min_length=8)
#
#     def create(self, validated_data):
#         user = User.objects.create_user(validated_data['username'], validated_data['email'],
#                                         validated_data['password'])
#         return user
#
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'email', 'password')