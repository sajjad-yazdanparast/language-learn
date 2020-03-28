from django.urls import path 
from . import views 
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('',views.test.as_view(),name='index') ,
    path('test/',views.test.as_view(),name='test') ,
    path('student/sign_in',views.StudentSignin.as_view(),name='student sign in'),
    path('student/get_token',views.StudentGetToken.as_view(),name='student get token') ,
]