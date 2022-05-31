from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
  categories = Category.objects.all() 

  return render(request, 'main/index.html', locals())

def categorySlide(request, slug):
  category = Category.objects.get(slug=slug)
  images = Image.objects.filter(category=category).order_by('-date_created')

  for x in images:
    x.shortDescription = x.description[:120]

  return render(request, 'main/category.html', locals())

def imageDetail(request, slug1, slug2):

  category = Category.objects.get(slug=slug1)
  image = Image.objects.get(slug=slug2)

  return render(request, 'main/image-detail.html', locals())

    


def search_image(request):
  if request.method == 'POST':
    searched = request.POST['searched']
    images = Image.objects.filter(title__contains=searched)
    return render(request, 'main/search.html', locals())
  else:
    return render(request, 'main/search.html', locals())
