from rest_framework import viewsets
from .models import Student
from .serializers import StudentSer

# This class is used for defining that all CRUD operations can be perform by using only this class
# and the given parameter (viewsets.ModelViewSet).

# ModelViewSet is bieng inherited from viewsets class which is import from rest_framework.

class StudentVS(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSer