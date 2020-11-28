from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Signup(models.Model):
    
    #user= models.ForeignKey(User ,null=True,  on_delete=models.CASCADE )
    name=models.CharField(max_length=122 )
    dob=models.DateField()
    email=models.EmailField(max_length=122)
    phone=models.IntegerField()

    def __str__(self):
        return self.name