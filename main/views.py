import json

from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View

from main.models import Shopping_Cart, Image, Product, Comment


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def product(request):
    return render(request, 'product.html')


def blog(request):
    return render(request, 'blog.html')


def feature(request):
    return render(request, 'feature.html')


def testimonial(request):
    return render(request, 'testimonial.html')


def contact(request):
    return render(request, 'contact.html')


def login(request):
    return render(request, 'login.html')


def shop(request):
    return render(request, 'shopping_cart.html')


def search(request):
    return render(request, 'search.html')


class ShoppingCartTemplateView(View):
    template_name = 'shopping_cart.html'
    context = {}

    def get(self, request):
        if request.user.id is None:
            return redirect('/accounts/login')
        shopping_cart = Shopping_Cart.objects.filter(user=request.user)
        data = []
        for index, value in enumerate(shopping_cart):
            image = Image.objects.filter(product=value.product).first()
            value.img = image
            value.index = index + 1
            data.append(value)
        self.context.update({'shopping_cart_products': data})
        return render(request, self.template_name, self.context)

    def post(self, request):
        shopping_cart_id = request.POST.get('shopping_cart_id')
        Shopping_Cart.objects.get(pk=shopping_cart_id).delete()
        return redirect('/shopping_cart')


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
        if not Shopping_Cart.objects.filter(Q(user=user) & Q(product=service_id)).exists():
            shopping_cart = Shopping_Cart.objects.create(
                user=user, product_id=service_id
            )
            shopping_cart.save()
            messages.info(request, 'Product added successfully !!!')
            return redirect(f'/')

        messages.error(request, 'This service already exists in cart')
        return redirect(f'/')


class AddProductView(View):
    template_name = "Add_Product.html"
    context = {}

    def get(self, request):
        return render(request, self.template_name, self.context)

    def post(self, request):
        title = request.POST.get('title')
        description = request.POST.get('desc')
        price = request.POST.get('price')
        old_price = request.POST.get('old_price')
        image = request.FILES.getlist('images')

        product = Product.objects.create(
            title=title,
            description=description,
            price=price,
            old_price=old_price,
            author_id=request.user
        )
        product.save()
        for image in image:
            img = Image.objects.create(
                img=image,
                product_id=product
            )
            img.save()
        return redirect('/add_product')


class IncrementCountAPIView(View):

    def post(self, request):
        try:
            json_data = json.loads(request.body.decode('utf-8'))
            shopping_cart_id = json_data.get('id')
            shopping_cart = Shopping_Cart.objects.get(pk=shopping_cart_id)
            shopping_cart.count += 1
            shopping_cart.save()
        except Exception as e:
            return JsonResponse({'success': False, 'error': e})
        return JsonResponse({'success': True})


class DecrementAPIView(View):
    def post(self, request):
        try:
            json_data = json.loads(request.body.decode('utf-8'))
            shopping_cart_id = json_data.get('id')
            shopping_cart = Shopping_Cart.objects.get(pk=shopping_cart_id)
            if shopping_cart.count > 0:
                shopping_cart.count -= 1
                shopping_cart.save()
        except Exception as e:
            return JsonResponse({'success': False, 'error': e})
        return JsonResponse({'success': True})


class ChangeCountAPIView(View):
    def post(self, request):
        try:
            json_data = json.loads(request.body.decode('utf-8'))
            shopping_cart_id = json_data.get('id')
            product_count = json_data.get('product_count')
            shopping_cart = Shopping_Cart.objects.get(pk=shopping_cart_id)
            if product_count is not None:
                shopping_cart.count = product_count
                shopping_cart.save()
        except Exception as e:
            return JsonResponse({'success': False, 'error': e})
        return JsonResponse({'success': True})


class CommentView(View):
    template_name = 'comment.html'
    context = {}

    def get(self, request):
        return render(request, self.template_name, self.context)

    def post(self, request):
        message = request.POST.get('message')
        is_anonymous = request.POST.get('is_anonymous')
        user = None if is_anonymous == 'on' else request.user
        comment = Comment.objects.create(
            message=message,
            user=user
        )
        comment.save()
        return redirect('/')


class CommentAnswerView(View):
    template_name = 'testimonial.html'
    context = {}

    def get(self, request):
        comments = Comment.objects.all()
        self.context.update({"comments": comments})
        return render(request, self.template_name, self.context)
