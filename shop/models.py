import address
from django.db import models
from django.core.validators import MaxValueValidator , MinValueValidator
import datetime

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Product(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=100, default= '', blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=0 , default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to = 'uploads/product/')

    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(max_digits=12, decimal_places=0 , default=0)

    star = models.IntegerField(default=0 , validators=[MinValueValidator(0), MaxValueValidator(5)])

    def __str__(self):
        return self.name



class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(default='', blank=False, max_length=150)
    phone = models.CharField(blank=True, max_length=15)
    date = models.DateTimeField(default=datetime.datetime.today())
    status = models.BooleanField(default=False)


    def __str__(self):
        return self.product