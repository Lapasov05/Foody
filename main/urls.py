from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import Shopping_Cart
from .views import *
from main.models import *

urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('product', ProductTemplateView.as_view(), name='products'),
    path('blog', blog, name='blog'),
    path('feature', feature, name='feature'),
    path('testimonial', CommentAnswerView.as_view(), name='testimonial'),
    path('contact', contact, name='contact'),
    path('login', login, name='login'),
    path('search', search, name='search'),
    path('shopping_cart',ShoppingCartTemplateView.as_view(),name='ShoppingCart'),
    path('add_product',AddProductView.as_view(),name='add_product'),
    path('comment',CommentView.as_view(),name='comment'),

    #API
    path('increment',csrf_exempt(IncrementCountAPIView.as_view()),name='increment'),
    path('decrement',csrf_exempt(DecrementAPIView.as_view()),name='decrement'),
    path('change',csrf_exempt(ChangeCountAPIView.as_view()),name='change'),

]
