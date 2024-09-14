from mongoengine import Document, StringField, IntField

# This class is defining the collections in our Document (MongoDB)

class Student(Document):
    name = StringField(required=True, max_length=200)
    Class = StringField(required=True, max_length=50)
    Marks = IntField(required=True)

    # It is used for determining that in this collection name we want to save our data.

    meta = {'collection': 'students'} 

