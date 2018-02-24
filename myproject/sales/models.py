from django.db import models
from django.conf import settings


# Create your models here.

class product(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    price = models.IntegerField()
    quantity = models.IntegerField()
    pos = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)


    @property
    def owner(self):
        return self.user
