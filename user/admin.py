from django.contrib import admin
from user.models import teacher,student
# Register your models here.

admin.site.register(student)
admin.site.register(teacher)