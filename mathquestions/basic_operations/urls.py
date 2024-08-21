from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.addNumber, name='name1'),
    path('average/', views.averageNumber, name='name2'),
    path('product/', views.productNumber, name='name3'),
]