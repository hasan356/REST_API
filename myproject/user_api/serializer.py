from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator,ValidationError
from django.db.models import Q

User = get_user_model()

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username' ,  'email' ,'password' ]

        extra_kwargs = {"password" : {"write_only" : True}}

        def create(self , validated_data):
            username = validated_data['username']
            email = validated_data['email']
            password = validated_data['password']
            user_obj = User( username = username , email = email)
            user_obj.setpassword(password)
            user_obj.save()
            return validated_data


class UserLoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False , allow_blank=True)
    # email = serializers.EmailField(label = 'Email Address' , required=False , allow_blank=True)
    token = serializers.CharField(allow_blank= True , read_only=True)
    class Meta:
        model = User
        fields = ['username' , 'password'  , 'token']

        extra_kwargs = {"password" : {"write_only" : True}}

    def validate(self , data):
        user_obj = None
        username = data.get('username')
        password = data['password']
        if not username:
            raise ValidationError("A username must exist to login")

        user = User.objects.filter(Q(username = username)).distinct()
        if user.exists() and user.count()==1:
            user_obj = user.first()
        else:
            raise ValidationError("Username is not valid")

        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError("Incorrect credentials try again")

        data["token"] = "Random"
        # username = validated_data['username']
        # email = validated_data['email']
        # password = validated_data['password']
        #
        # user_obj = User( username = username , email = email)
        # user_obj.setpassword(password)
        # user_obj.save()
        return data

