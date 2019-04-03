from django.db import models
import datetime
from django.contrib.auth.models import User


class UserShell(models.Model):
    name = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=150, blank=True)
    phone = models.CharField(max_length=10, blank=True)
    email = models.EmailField(blank=True)


    def __str__(self):
        return self.name

class ServerReply(models.Model):
    id = models.IntegerField(primary_key=True)
    replyText = models.CharField(max_length=100, blank=True)
    alreadyExists = models.BooleanField(default= False)

    def __str__(self):
        return self.id

class Commands(models.Model):
    id = models.IntegerField(primary_key=True)
    command = models.CharField(max_length=10)
    paramters = models.CharField(max_length=10)
    alreadyExists = models.BooleanField(default= False)
    argumentsProv = models.CharField(max_length=20)
    isPiped = models.BooleanField(default= False)
    userid = models.IntegerField(default=0)
    isAlais = models.BooleanField(default= False)
    orginal = models.CharField(max_length=10, blank=True)
    pastaComments = models.CharField(max_length=100, blank=True)
    isRoot = models.BooleanField(default= False)
    ServerReply = models.ManyToManyField(ServerReply, blank=True)
    UserShell = models.ForeignKey(UserShell, on_delete=models.CASCADE, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.command


