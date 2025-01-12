from django.db import models
from users.models import Users

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 255)

    def __str__(self):
        return self.name

class Products(models.Model):
    values = (("gold", "Gold"), ("silver", "Silver"))
    name = models.CharField(max_length = 255)
    description = models.TextField()
    type = models.CharField(choices = values, max_length = 10, default = "Gold")
    weight = models.FloatField()
    image = models.ImageField(upload_to = "images/")
    category = models.ForeignKey(Category, related_name = "products", on_delete = models.CASCADE)

    def __str__(self):
        return self.name + " " + str(self.weight)
    
    class Meta:
        verbose_name_plural = 'Category'

    # use the function name to while accessing image "imageURL"
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class GoldPrice(models.Model):
    gold = models.FloatField(default = 1927.32)
    date_added = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return str(self.gold)
    
    class Meta:
        verbose_name_plural = 'GoldPrice'

class Price(models.Model):
    product = models.ForeignKey(Products, related_name='price', on_delete=models.CASCADE)
    gold_price = models.ForeignKey(GoldPrice, related_name= "price", on_delete = models.CASCADE)

    # "get_product_price" returns calculated total price of product
    @property
    def get_product_price(self):
        return self.product.weight*self.gold_price.gold
    
    def __str__(self):
        return self.product.name
    

    class Meta:
        verbose_name_plural = 'Price'