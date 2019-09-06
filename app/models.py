from django.db import models
from django.contrib.auth.models import AbstractUser

# class CustUser(AbstractUser):
#     pass

class product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)


class offer(models.Model):
    Code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    discount = models.FloatField()