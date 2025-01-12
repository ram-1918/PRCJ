from django.db import models
from users.models import Users
from products.models import Category, Products, GoldPrice, Price

# Create your models here.
class Orders(models.Model):
    values = (('Order Placed', 'Orderplaced'),('Creating','creating'), ('Completed', 'completed'), ('Shipped', 'shipped'))
    users = models.ForeignKey(Users, related_name = "orders", on_delete = models.CASCADE)
    status = models.CharField(choices = values, max_length = 20, default = 'Order Placed')
    date_added = models.DateTimeField(auto_now_add= True)
    transaction_id = models.CharField(max_length = 255)

    @property
    def get_cart_total(self):
        total = 0
        for item in self.orderitem.all():
            total += item.get_total_per_quantity
        return total

    @property
    def no_of_items_in_cart(self):
        items = self.orderitem.all()
        return sum([i.quantity for i in items])

    def __str__(self):
        return f"Order {self.pk}"
    
    class Meta:
        verbose_name_plural = 'Orders'

class OrderItem(models.Model):
    order = models.ForeignKey(Orders, related_name = "orderitem", on_delete = models.CASCADE)
    product = models.ForeignKey(Price, related_name= "orderitem",  on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField(default = 0, blank = True, null = True)
    date_added = models.DateTimeField(auto_now_add= True)

    # gets the price for the given quantity which can be retrieved by frontend using "get_total" function
    @property
    def get_total_per_quantity(self):
        total = self.product.get_product_price*self.quantity
        return total

    # def save(self, *args, **kwargs):
    #     self.price = self.quantity * self.product.price
    #     super(OrderItem, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.quantity}x{self.product.price}'

    class Meta:
        verbose_name_plural = 'OrderItem'

