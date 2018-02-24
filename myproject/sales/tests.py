from django.test import TestCase
from rest_framework.test import APITestCase
# Create your tests here.
from django.contrib.auth import get_user_model

from .models import product

User = get_user_model()

class salesAPITestCase(APITestCase):
    def setup(self):
        user_obj = User(username = 'test' , email = 'test@test.com')
        user_obj.set_password("somepassword")
        user_obj.save()
        list = product.objects.create(user = user_obj ,
                                      name = 'lays' ,
                                      price = 34 ,
                                      quantity = 4 ,
                                      pos = 'A4')


    # def test_single_user(self):
    #      user_count = User.objects.count()
    #      self.assertEqual(user_count,1)

    # def test_single_items(self):
    #      items_count = product.objects.count()
    #      self.assertEqual(items_count  ,1)