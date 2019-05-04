from django.urls import path
from . import views

#this link url to  /products->this app


urlpatterns = [
    path('', views.index),
    path('new/', views.new)
]