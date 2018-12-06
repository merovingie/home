from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    image = models.ImageField(upload_to = 'images/')
    radius = models.IntegerField(default= 1)
    title = models.CharField(max_length = 50)
    

    def __str__(self):
        return f'{self.title}'