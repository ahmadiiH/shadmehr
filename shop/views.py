from django.shortcuts import render , HttpResponse
from .models import Product

# Create your views here.
def helloworld(request):
    all_products = Product.objects.all()
    return render(request,"index.html",{'products':all_products})

def about(request):
    return render(request,'about.html',{})