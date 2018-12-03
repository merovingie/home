from django.db import models
from django.contrib.auth.models import User

class Job(models.Model):
    image = models.ImageField(upload_to = 'images/')
    summary = models.CharField(max_length = 200)
    title = models.CharField(max_length = 50)
    url = models.CharField(max_length= 200)

    def __str__(self):
        return f'{self.title}'