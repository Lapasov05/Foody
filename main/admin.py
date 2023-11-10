from django.contrib import admin
from .models import Shopping_Cart,Product,Image

admin.site.register((Product,Image,Shopping_Cart))
