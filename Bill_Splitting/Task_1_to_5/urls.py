from django.urls import path
from . import views

urlpatterns = [
    path('evenlysplit/', views.split_evenly, name='split_evenly'),
    path('unevenlysplit/', views.split_unevenly, name='split_unevenly'),
    path('splitincludingtipandtax/', views.split_including_tip_and_tax, name='split_including_tip_and_tax'),
    path('splitwithdiscount/', views.split_with_discount, name='split_with_discount'),
    path('splitwithshareditems/', views.split_with_shareditems, name='split_with_shareditems'),
]