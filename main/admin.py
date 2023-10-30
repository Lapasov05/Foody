from django.contrib import admin
from .models import Shopping_Cart,Product,Image,Todos

admin.site.register((Product,Image,Shopping_Cart,Todos))
