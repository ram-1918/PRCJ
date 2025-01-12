from collections import defaultdict
from django.db import models

class item_models(models.Model):    
    item_id = models.CharField(max_length=100)
    item_type=models.CharField(max_length=100)
    item_image = models.ImageField(upload_to="allmodels")
    item_weight = models.IntegerField()
    item_status= models.BooleanField(default=False)


class wishlist(models.Model):
    devicename=models.CharField(max_length=100)
    item_id=models.CharField(max_length=100)
    item_type=models.CharField(max_length=100)
    item_status= models.BooleanField(default=False)




