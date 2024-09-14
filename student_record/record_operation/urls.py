# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import BookViewSet

# router = DefaultRouter()
# router.register(r'books', BookViewSet, basename='book')

# # /books GET
# # /books POST
# # /books/:id GET
# # /books/:id PUT
# # /books/:id DELETE

# urlpatterns = [
#     path('', include(router.urls)),
# ]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentVS

router = DefaultRouter()
router.register(r'students', StudentVS, basename='student') 

urlpatterns = [
    path('', include(router.urls)),
]
