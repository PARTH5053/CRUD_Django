from django.db import models
from django.contrib.auth.models import User


class Records(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    phone = models.IntegerField()
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=50)
    province = models.CharField(max_length=50) 
    country = models.CharField(max_length=50)   

    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name+" "+self.last_name
    