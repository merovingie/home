from django.db import models


class D3model(models.Model):
    r = models.IntegerField(default= 1)
    cx = models.IntegerField(default= 10)
    cy = models.IntegerField(default= 10)
    fill = models.CharField(max_length = 50)
    title = models.CharField(max_length = 50)
    type = models.CharField(max_length = 50)
    

    def __str__(self):
        return f'{self.title}+' '+{self.type}'
        