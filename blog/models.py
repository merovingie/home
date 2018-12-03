from django.db import models

class Blog(models.Model):
    image = models.ImageField(upload_to = 'images/')
    body = models.CharField(max_length = 200)
    title = models.CharField(max_length = 50)
    pub_date = models.Datetime
    def __str__(self):
        return f'{self.title}'