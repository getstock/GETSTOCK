from django.db import models

class Account(models.Model):
    login = models.CharField(max_length = 30)
    password = models.CharField(max_length = 30)
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    email = models.CharField(max_length = 30)
    stocks = models.ManyToManyField("market.stock")
# Create your models here.
