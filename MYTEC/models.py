from django.db import models
from django.conf import settings 
import os
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User

User = settings.AUTH_USER_MODEL

def MYTEC_directory_path(instance, filename):
   banner_pic_name='MyTec/produScts/{0}/{1}'.format(instance.name, filename) 
   full_path = os.path.join(settings.MEDIA_ROOT, banner_pic_name)
   
   if os.path.exists(full_path): 
       os.remove(full_path)
       
   return banner_pic_name

class SearchManager(models.Manager):
   def search(self, query):
       return self.get_queryset().filter(name__icontains=query)

class Product(models.Model):
   name = models.CharField(max_length=200)
   user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="products") 
   name = models.CharField(max_length=100)
   description=models.TextField()
   thumbnail = models.ImageField(blank=True, null=True, upload_to=MYTEC_directory_path)
  
   active = models.BooleanField(default=False)

   price = models.PositiveIntegerField(default=100) #cents Cont be lower than 50 cents@l

   objects = models.Manager() # El manager predeterminado.
   search = SearchManager()
   
   def str(self):
       return self.name
   
   def price_display(self):
       return "{0:.2f}".format(self.price / 100)

class PurchasedProduct (models.Model):
   email = models. EmailField()
   product = models.ForeignKey(Product, on_delete=models.CASCADE)
   date_purchased = models.DateTimeField(auto_now_add=True)
       
   def _str_(self):
       return self.email
   
