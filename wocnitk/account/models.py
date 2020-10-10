from django.db import models
from django.contrib.auth.models import User,auth
# Create your models here.

class branch(models.Model):
    name = models.CharField(max_length=30,blank=True, null=False)
    def __str__(self):
        return self.name
class userdetails(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    branch = models.ForeignKey(branch, on_delete=models.CASCADE)
    batch=models.IntegerField(default=2020)