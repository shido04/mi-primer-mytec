
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings 
from django.urls.conf import include
from . import views



from .views import (
HomeView, 
UserProductListView, 
ProductUpdateView, 
ProductDetailView, 
CreateCheckoutSessionView,
SuccessView,
stripe_webhook,
UserLibraryView,
SearchView,





)

urlpatterns = [
    
     path('search/', SearchView.as_view(), name='search'),
     
     

     path('create-checkout-session/', CreateCheckoutSessionView.as_view(), name="create-checkout-session"),
     path('products/<int:pk>/', ProductDetailView.as_view(), name="product-detail"),
     path('admin/', admin.site.urls),
     path('accounts/', include('allauth.urls')),
     path('users/', include('accounts.urls', namespace='users')),
     path('success/', SuccessView.as_view(), name="success"),
     path("library/<username>/", UserLibraryView.as_view(), name="library"),
     path("webhooks/stripe/", stripe_webhook, name="stripe-webhook"),
     path('', HomeView.as_view(), name="home"),
     path('products/', UserProductListView.as_view(), name="product-list"),
     path('products/update/<int:pk>/', ProductUpdateView.as_view(), name="product-update"),
     path('MYTEC/', include('MYTEC.urls', namespace="MYTEC")),
   


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)