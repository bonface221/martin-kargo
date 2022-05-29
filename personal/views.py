from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
  category = Category.objects.all()
  return render(request, 'main/index.html', locals())

def categorySlide(request, slug):
  category = Category.objects.get(slug=slug)
  images = Image.objects.filter(category=category)

  for x in images:
    x.shortDescription = x.description[:120]

  return render(request, 'main/', locals())
