from django.db import models
import datetime
from django.contrib.auth.models import User

class UserShell(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

class ServerReply(models.Model):
    id = models.IntegerField(primary_key=True)
    replyText = models.CharField(max_length=100)
    alreadyExists = models.BooleanField()

    def __str__(self):
        return self.id

class Commands(models.Model):
    id = models.IntegerField(primary_key=True)
    command = models.CharField(max_length=10)
    paramters = models.CharField(max_length=10)
    alreadyExists = models.BooleanField()
    argumentsProv = models.CharField(max_length=20)
    isPiped = models.BooleanField()
    userid = models.IntegerField()
    isAlais = models.BooleanField()
    orginal = models.CharField(max_length=10)
    pastaComments = models.CharField(max_length=100)
    isRoot = models.BooleanField()
    ServerReply = models.ManyToManyField(ServerReply)
    UserShell = models.ForeignKey(UserShell, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.command

