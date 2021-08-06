from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class ExtendedUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    lastLogin = models.DateTimeField(auto_now_add=True)
    noOfLogin=models.IntegerField(default=0)
    timestamp = models.TimeField(auto_now_add=True)
    #timestamp.editable = True
    #lastLogin.editable= True
    def __str__(self):
        return self.user.username


class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(blank=False, max_length=300)
    title = models.CharField(blank=False, max_length=300)
    content = models.CharField(blank=False, max_length=8000)
    tag=models.CharField(blank=True, max_length=300)
    time = models.TimeField(auto_now_add=True, editable=True)
    date= models.DateField(auto_now_add=True, editable=True)
    image= models.ImageField(upload_to="media", blank=True)
    #time.editable = True
    #date.editable =True
    def __str__(self):
        return self.name
