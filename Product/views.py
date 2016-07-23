from django.shortcuts import render
from django.http import HttpResponse
from django.views import  generic, View
#from .models import Category


# Create your views here.
def index(request):
    
    return HttpResponse("Welcome to shopinum");
class IndexView(generic.ListView):
    pass
    #model = Category
    #template_name = "product/index.html"
    
class Registration(View):
    pass
    
    