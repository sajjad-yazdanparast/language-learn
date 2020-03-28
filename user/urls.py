from django.urls import path
from django.conf.urls import url
from . import views 
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token


urlpatterns = [
    path('',views.test.as_view(),name='index') ,
    path('test/',views.jwt_test.as_view(),name='test') ,
    path('student/sign_in',views.StudentSignin.as_view(),name='student sign in'),
    path('student/get_token',views.StudentGetToken.as_view(),name='student get token') ,

    url(r'^auth-jwt/', obtain_jwt_token),
    url(r'^auth-jwt-refresh/', refresh_jwt_token),
    url(r'^auth-jwt-verify/', verify_jwt_token),
]