from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.response import Response 
from rest_framework.decorators import APIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework import status
from .models import student,teacher
from .serializers import student_srializer,teacher_serializer   
import jwt
from rest_framework_jwt.utils import jwt_payload_handler
from soft_pro_test import settings
# Create your views here.


def create_token(user):
    payload = jwt_payload_handler(user)
    token = jwt.encode(payload, settings.SECRET_KEY)
    return token.decode('unicode_escape')

class test(APIView) :
    permission_classes = (IsAuthenticated,)

    def get(self,request) :
        return Response({'message':'hallo Mann'}) 


class jwt_test(APIView):
    permission_classes = (IsAuthenticated,) 
    def get(self,request):
        return Response(status=status.HTTP_200_OK,data={'user':request.user.username})

class StudentSignin(APIView) :

    permission_classes = (AllowAny,)

    def post(self,request) :
        try:
            serialed = student_srializer(data=request.data)
            if serialed.is_valid() :
                if User.objects.filter(username=request.data['username']).exists() :
                    return Response(data={'message':'duplicated username not allowed'},status=status.HTTP_200_OK)

                user = User.objects.create_user(username=request.data['username'],password=request.data['password'])
                token = create_token(user)
                stu = student.objects.create(person=user,token=token)
                stu.save()
                return Response({'message':'user created successfully!','token':str(token)},status=status.HTTP_201_CREATED)
            return Response({'message':'input not valid'},status=status.HTTP_400_BAD_REQUEST)
        except :
            return Response({'message':'something went wrong'},status=status.HTTP_400_BAD_REQUEST)


class StudentLogin(APIView) :
    permission_classes = (AllowAny,) 

    def post(self,request):
        try :
            serialed = student_srializer(data=request.data) 
            if serialed.is_valid() :
                username_requested  = request.data['username']
                try :
                    user = User.objects.filter(username=username_requested)[0]
                except :
                    return Response({'message':'username not exist'},status=status.HTTP_404_NOT_FOUND)
                if not (user is None):
                    if user.check_password(request.data['password']) :
                        token = str(student.objects.filter(person=user)[0].token)
                        return Response({'token':token},status=status.HTTP_200_OK)
                    else :
                        return Response({'message':'wrong password'},status=status.HTTP_400_BAD_REQUEST)
        except :
            return Response({'message':'something went wrong'},status=status.HTTP_400_BAD_REQUEST)

class StudentGetToken(APIView) :
    permission_classes = (AllowAny,)

    def post(self,request) :
        serialed = student_srializer(data=request.data)
        if serialed.is_valid() :
            user = User.objects.filter(username=request.data['username'])[0]
            if not (user is None) :
                token = str(student.objects.filter(person = user)[0].token)
                return Response({'token':token},status=status.HTTP_200_OK)
            return Response({'message':'user not found'},status=status.HTTP_404_NOT_FOUND)
        return Response({'message':'invalid input'},status=status.HTTP_400_BAD_REQUEST)
