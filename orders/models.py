from django.db import models

# Create your models here.

class OrderDetails(models.Model):
    customer_id = models.IntegerField()
    customer_name = models.CharField(max_length=100)
    restaurant_id = models.IntegerField()
    center_id = models.IntegerField(null=True,default=1)
    item_name = models.CharField(max_length=50)
    product_price = models.FloatField()
    latitude = models.FloatField()
    longitude = models.FloatField()

class centerRestaurantMapping(models.Model):
    center_id = models.IntegerField()
    restaurant_id = models.IntegerField()
    location = models.CharField(default='Kormangala',max_length=50)