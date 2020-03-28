from rest_framework import serializers 
from.models import student,teacher

class student_srializer(serializers.ModelSerializer) :
    class Meta :
        model = student 
        fields = ()

class teacher_serializer(serializers.ModelSerializer):
    class Meta:
        model = teacher 
        fields = ()