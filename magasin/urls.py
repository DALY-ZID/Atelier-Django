from django.urls import path,include
from django.contrib import admin
from . import views
from .views import CategoryAPIView, ProductAPIView

urlpatterns = [
    path('', views.index , name = 'index'),
    path('addPrd/', views.AddProduct , name = 'addPrd'),
    path('addFrs/', views.AddFrs , name = 'addFrs'),
    path('addCmd/', views.AddCmd , name = 'addCmd'),
    path('frs/', views.ListFrs , name = 'frs_list'),
    path('product/', views.ListPrd, name = 'product_list'),
    path('commandes/', views.ListCmd, name = 'commande_list'),
    path('register/',views.register, name = 'register'), 
    path('api/category/', CategoryAPIView.as_view()),
    path('api/product/', ProductAPIView.as_view())


]