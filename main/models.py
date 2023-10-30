from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()



class Product(models.Model):
    title = models.CharField(max_length=255)
    # description = models.TextField()
    price = models.FloatField()
    old_price=models.FloatField()
    # image = models.ImageField(upload_to='picture',blank=True,null=True,)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.title


class Todos(models.Model):
    text = models.TextField()
    expires_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Todo'
        verbose_name_plural = 'Todos'

    def __str__(self):
        return f'{self.text} from {self.owner}'


class Image(models.Model):
    img = models.ImageField(upload_to='picture')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Shopping_Cart(models.Model):
    product =models.ForeignKey(Product,on_delete=models.CASCADE)
    user =models.ForeignKey(User,on_delete=models.CASCADE)
    upload_at = models.DateTimeField(auto_now_add=True)
    count = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.product.title} from {self.user.username}'



