from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('category/<slug:slug>', views.categorySlide, name='image-category'),
  path('category/<slug:slug1>/<slug:slug2>', views.imageDetail, name='image-details'),
  path('search/', views.search_image, name='search-image'),

]