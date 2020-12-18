from django.db import models
from django.db.models import Sum
class Product(models.Model):
    description = models.CharField(max_length=45)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"<Product Object: Price: {self.price} | {self.description}>"

class Order(models.Model):
    quantity_ordered = models.IntegerField()
    total_price = models.DecimalField(decimal_places=2, max_digits=6)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"Order Object: id: {self.id} | quantity_ordered: {self.quantity_ordered} | total price {self.total_price}"

class User_Order(models.Model):
    total_spending = Order.objects.aggregate(Sum('total_price'))


    