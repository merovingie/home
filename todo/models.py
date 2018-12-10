from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    # image = models.ImageField(upload_to = 'images/')
    r = models.IntegerField(default= 1)
    cx = models.IntegerField(default= 10)
    cy = models.IntegerField(default= 10)
    # z = models.IntegerField(default= 10)
    # len1 = models.IntegerField(default= 10)
    # len2 = models.IntegerField(default= 10)
    # len3 = models.IntegerField(default= 10)
    fill = models.CharField(max_length = 50)
    

    def __str__(self):
        return f'{self.fill}'
        