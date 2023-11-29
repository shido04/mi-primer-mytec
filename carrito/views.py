from django.shortcuts import render,redirect
from .models import Product, Cart, CartItem
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def add_to_cart(request, product_id):
   product = Product.objects.get(pk=product_id)
   cart, created = Cart.objects.get_or_create(user=request.user)
   cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)
   
   if not item_created:
       cart_item.quantity += 1
       cart_item.save()
   
   return redirect('product-list')
