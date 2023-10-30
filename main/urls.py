from django.urls import path

from .views import Shopping_Cart
from .views import *
from main.models import *

urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('product', ProductTemplateView.as_view(), name='products'),
    path('blog', blog, name='blog'),
    path('feature', feature, name='feature'),
    path('testimonial', testimonial, name='testimonial'),
    path('contact', contact, name='contact'),
    path('login', login, name='login'),
    path('search', search, name='search'),
    path('shopping_cart',ShoppingCartTemplateView.as_view(),name='ShoppingCart')


]
