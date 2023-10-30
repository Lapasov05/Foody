from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views import View

from main.models import Shopping_Cart, Image, Product, Todos


def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def product(request):
    return render(request,'product.html')

def blog(request):
    return render(request,'blog.html')

def feature(request):
    return render(request,'feature.html')

def testimonial(request):
    return render(request,'testimonial.html')

def contact(request):
    return render(request,'contact.html')

def login(request):
    return render(request,'login.html')

def shop(request):
    return render(request,'shopping_cart.html')

def search(request):
    return render(request,'search.html')

class ShoppingCartTemplateView(View):
    template_name = 'shopping_cart.html'
    context = {}

    def get(self, request):
        if request.user.id is None:
            return redirect('/accounts/login')
        shopping_cart = Shopping_Cart.objects.filter(user=request.user)
        data = []
        for index, value in enumerate(shopping_cart):
            image = Image.objects.filter(service=value.service).first()
            value.img = image
            value.index = index + 1
            data.append(value)
        self.context.update({'shopping_cart_products': data})
        return render(request, self.template_name, self.context)

    def post(self, request):
        shopping_cart_id = request.POST.get('shopping_cart_id')
        Shopping_Cart.objects.get(pk=shopping_cart_id).delete()
        return redirect('/shopping-cart')




class HomeTemplateView(View):
    template_name = 'index.html'
    context = {}

    def get(self, request):
        todos_data = Todos.objects.all()
        self.context.update({'todos_data': todos_data})
        return render(request, self.template_name, self.context)

    def post(self, request):
        pass
class ProductTemplateView(View):
    template_name = 'product.html'
    context = {}

    def get(self, request):
        service_data = Product.objects.all()
        # comments = Comment.objects.all().order_by('-created_at')[:4]
        services_data = []
        for service in service_data:
            image = Image.objects.filter(product=service).first()
            service.image = image
            services_data.append(service)
        self.context.update({'product_data': services_data})
        # self.context.update({'comments': comments})
        return render(request, self.template_name, self.context)

    def post(self, request):
        service_id = request.POST.get('service_id')
        user = request.user
        if not Shopping_Cart.objects.filter(Q(user=user) & Q(service_id=service_id)).exists():
            shopping_cart = Shopping_Cart.objects.create(
                user=user, service_id=service_id
            )
            shopping_cart.save()
            messages.info(request, 'Product added successfully !!!')
            return redirect(f'/#service_{service_id}')

        messages.error(request, 'This service already exists in cart')
        return redirect(f'/#service_{service_id}')