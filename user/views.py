from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.response import Response 
from rest_framework.decorators import APIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework import status
from .models import student,teacher
from .serializers import student_srializer,teacher_serializer
# Create your views here.

class test(APIView) :
    permission_classes = (IsAuthenticated,)

    def get(self,request) :
        return Response({'message':'hallo Mann'}) 

    
class StudentSignin(APIView) :

    permission_classes = (AllowAny,)

    def post(self,request) :
        serialed = student_srializer(data=request.data)

        if serialed.is_valid() :
            if User.objects.filter(username=request.data['username']).exists() :
                return Response(data={'message':'duplicated username not allowed'},status=status.HTTP_400_BAD_REQUEST)
        
            user = User.objects.create_user(username=request.data['username'],password=request.data['password'],first_name='sajjad',last_name='yazdanparast')
            token , _ = Token.objects.get_or_create(user=user)
            stu = student.objects.create(person=user)
            stu.save()
            return Response({'message':'user created successfully!' ,'token' :token.key},status=status.HTTP_200_OK)
        return Response({'message':'input not valid'},status=status.HTTP_400_BAD_REQUEST)



class StudentGetToken(APIView) :
    permission_classes = (AllowAny,)

    def post(self,request) :
        serialed = student_srializer(data=request.data)
        if serialed.is_valid() :
            user = User.objects.filter(username=request.data['username'])[0]
            if not (user is None) :
                token , _  = Token.objects.get_or_create(user=user)
                return Response({'token':token.key},status=status.HTTP_200_OK)
            return Response({'message':'user not found'},status=status.HTTP_404_NOT_FOUND)
        return Response({'message':'invalid input'},status=status.HTTP_400_BAD_REQUEST)
