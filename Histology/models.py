from django.db import models
from django.contrib.auth.models import User


class Entrynew(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    #date.editable = True
    time = models.TimeField(auto_now_add=True)
    #time.editable = True
    duration = models.TimeField()
    box_number= models.IntegerField(default=0)
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    authQuest = models.CharField(max_length = 10)
    message_field = models.CharField(max_length = 150)
    email_field = models.EmailField()
    date_created = models.DateTimeField(auto_now_add=True)
    Box_type = models.CharField(max_length = 6)
    cassettes_num = models.IntegerField(default=0)
    container_num = models.IntegerField(default=0)
    reqtotal_num = models.IntegerField(default=0)
    starting_DIDSTR = models.CharField(max_length= 11)
    starting_DID = models.BigIntegerField(default=0)
    ending_DID = models.BigIntegerField(default=0)
    problem_flag = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.date_created}'

class boxDisplayView(models.Model):
    ORANGE_DOT = 'OR'
    IN_HOUSE = 'IH'
    ORAL = 'OR'
    STAT = 'ST'
    PAS = 'PAS'
    ROH = 'RO'


    DID_CHOICES = (
        (STAT, 'Stat'),
        (ORAL, 'Oral'),
        (IN_HOUSE, 'In House'),
        (ORANGE_DOT, 'Orange Dot'),
    )

    DID_comments = (
        (PAS, 'Plasma Stain'),
        (ROH, 'RO Something'),
    )

    author_box = models.ForeignKey(User, on_delete=models.CASCADE)
    # author_name_box = models.ManyToManyField(Entrynew)
    cassettes = models.IntegerField(default=0)
    contianers = models.IntegerField(default=0)
    DID_num = models.BigIntegerField(default=0)
    # DID_num.editable = False
    DID_type = models.CharField(choices = DID_CHOICES, max_length= 30)
    DID_comments = models.CharField(choices = DID_comments, max_length= 30)
    DID_date_created = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return f'{self.DID_num} {self.DID_date_created}'



