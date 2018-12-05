import sys
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from home.models import products
def index(request):

    template=loader.get_template('index.html')
    posts="hello i ma vijay"
    all_product = products.objects.all()
    # #print(all_product)
    # for e in products.objects.all():
    #      print(e.id)
    #print(all_product)
    return render(request,'index.html',{'all_product': all_product})

def detail(request,page_id):
    return HttpResponse('<h1>your page _id'+page_id+'</h1>')