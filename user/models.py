from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class student(models.Model) :
    person = models.OneToOneField(User,on_delete=models.CASCADE)


    def __str__(self) : 
        return str(self.person.username)



class teacher(models.Model) :
    person = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__ (self):
        return str(self.person.username)