
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,UserManager,AbstractUser



class User(AbstractUser):
    phone = models.CharField(max_length=13)



class Province(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class SubProvince(models.Model):
    title = models.CharField(max_length=255)
    province = models.ForeignKey(Province, models.CASCADE)

    def __str__(self):
        return self.title


class Pump(models.Model):
    name = models.CharField(max_length=100000)
    info = models.TextField()
    StartDate = models.DateTimeField(auto_now_add=True)
    UpdateDate = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='media/',blank=True,null=True)
    province = models.ForeignKey(Province, models.SET_NULL, null=True, blank=True)
    subprovince = models.ForeignKey(SubProvince, models.SET_NULL, null=True, blank=True)
    umumiy_mal = models.FloatField(blank=True,null=True)
    oy_mal = models.FloatField(blank=True,null=True)
    kun_mal = models.FloatField(blank=True,null=True)
    soat_mal = models.FloatField(blank=True,null=True)

    def __str__(self):
        return self.name
    
    