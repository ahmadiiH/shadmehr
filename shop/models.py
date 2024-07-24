from django.db import models
import datetime
from django.core.validators import MinLengthValidator,MaxLengthValidator 
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) :
        return self.name

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email =models.EmailField(max_length=100)
    password =models.CharField(max_length=50)

    def __str__(self) :
        return f'{self.first_name} {self.last_name}'
    
class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50 , default="" , blank=True , null=True)
    price = models.DecimalField(max_digits=12, decimal_places=0, default=0)
    category =models.ForeignKey(Category,on_delete=models.CASCADE , default=1)
    picture =models.ImageField(upload_to="upload/product/")
    is_sale = models.BooleanField(default=False)
    sale_price =  models.DecimalField(max_digits=12, decimal_places=0, default=0)
    star = models.IntegerField(default=0) 

    def __str__(self) :
        return self.name
    
class Order(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    last_name = models.CharField(max_length=50)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=20, blank=True)
    email =models.EmailField(max_length=100)
    phone = models.CharField(max_length=20,blank=True)
    date = models.DateField(default=datetime.datetime.today())
    status = models.BooleanField(default=False)

    def __str__(self) :
        return self.product
    
