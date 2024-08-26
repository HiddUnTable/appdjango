from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.
class new_user(models.Model):
    full_name=models.CharField(max_length=150)
    birth_date=models.DateField()
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=100,blank=True)

    USERNAME_FIELD = 'email'

    class Meta:
        db_table = 'new_user'

class EmployeeAdd(models.Model):
    nip= models.CharField(max_length=25, unique = True)
    first_name= models.CharField(max_length=100)
    last_name= models.CharField(max_length=100)
    gender= models.CharField(max_length=1)
    birth_place= models.CharField(max_length=50)
    birth_date= models.DateField()
    address= models.TextField()
    phone_number= models.CharField(max_length=15)
    email= models.EmailField()
    date_joined= models.DateField()
    
    class Meta:
        db_table = 'employee'

    def __str__(self):
        return f"{self.first_name}{self.last_name}"