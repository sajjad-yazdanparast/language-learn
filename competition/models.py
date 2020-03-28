from django.db import models
from user.models import student
# Create your models here.
class competition (models.Model) :
    score = models.IntegerField()
    
    competitor_one = models.ForeignKey(student,on_delete=models.CASCADE,null=True ,related_name='competitor_one')
    competitor_two = models.ForeignKey(student,on_delete=models.CASCADE,null=True ,related_name='competitor_two')
    date = models.DateField()
