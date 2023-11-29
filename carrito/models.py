from django.db import models
from MYTEC.models import Product
from django.conf import settings 

User = settings.AUTH_USER_MODEL

# Create your models here.
class Cart(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   products = models.ManyToManyField(Product, through='CartItem')

   def __str__(self):
       return f"Cart for {self.user.username}"

class CartItem(models.Model):
   cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
   product = models.ForeignKey(Product, on_delete=models.CASCADE)
   quantity = models.PositiveIntegerField(default=1)

   def __str__(self):
       return f"{self.quantity} x {self.product.name}"
   
