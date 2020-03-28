from django.urls import path 
from competition import views

urlpatterns = [
    path('',views.index,name='index') ,
]
