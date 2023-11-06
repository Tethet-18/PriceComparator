from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.cart),
    path('addtocart/', views.addToCart),
    path('del/<str:id>',views.DeleteFromCart)
]
