from .models import Student
from rest_framework_mongoengine.serializers import DocumentSerializer
 
# DocumentSerializers is used for taking data by using rest_framework_mongoengine because our data 

# store in MongoDB and by using mongoengine we can easily save our data in MongoDB

class StudentSer(DocumentSerializer):
    class Meta:
        model = Student
        fields = '__all__'
