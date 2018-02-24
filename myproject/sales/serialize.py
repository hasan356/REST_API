from rest_framework import serializers
from .models import product

class salesSerializers(serializers.ModelSerializer):

    class Meta:
        model = product
        fields = ['pk' , 'user' , 'name' , 'price' ,'quantity' , 'pos']