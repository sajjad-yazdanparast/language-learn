from rest_framework import serializers 
from.models import student,teacher
from django.contrib.auth.models import User

class user_serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)

class student_srializer(serializers.ModelSerializer) :
    # person = user_serializer(required=True)
    class Meta :
        model = student 
        fields = ()

class teacher_serializer(serializers.ModelSerializer):
    class Meta:
        model = teacher 
        fields = ()