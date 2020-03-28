import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE','soft_pro_test.settings')
import django 
django.setup()


from user.models import student
from user.models import teacher
from competition.models import competition 
from faker import Faker
generator = Faker()
import numpy as np 


def populate_student(number:int=10) :
    for _ in range(number) :
        user_name = generator.user_name()
        phone_number = generator.phone_number()
        email = generator.email()
        # user_name = 'mohammad'
        # phone_number = '09123456789'
        # email = 'a@a.com'
        student.objects.get_or_create(user_name=user_name,phone_number=phone_number,email=email)
    

if __name__ == '__main__' :
    populate_student(20)
    print('population successful')