import sys
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from products.models import products

def index(request):
    objectsDtl = products.objects
   # print(objectsDtl.product_name)
    template=loader.get_template('index.html')
    return render(request,'products.html')

def detail(request,page_id):
    return HttpResponse('<h1>your page _id'+page_id+'</h1>')