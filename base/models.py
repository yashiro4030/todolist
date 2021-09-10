from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    systeme =models.CharField(max_length=50,null=True,blank=True)
    service = models.CharField(max_length=50,null=True,blank=True)
    check = models.BooleanField(default=False)
    create = models.DateTimeField(auto_now=True)
    action = models.TextField(max_length=200,null=True,blank=True)
    remarque = models.TextField(max_length=200,null=True,blank=True)

    def __str__(self) -> str:
        return self.systeme

    class Meta:
        ordering = ['check']   
