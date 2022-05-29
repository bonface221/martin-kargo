from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
  category = Category.objects.all()
  return render(request, 'main/index.html', locals())

def categorySlide(request):
  return render(request, 'main/', locals())
