from django.db import models

# Create your models here.
class Stock(models.Model):
    stock_name = models.CharField(max_length = 20)
    buy_cost = models.DecimalField(max_digits = 10, decimal_places = 3)
    sell_cost = models.DecimalField(max_digits = 10, decimal_places = 3)
