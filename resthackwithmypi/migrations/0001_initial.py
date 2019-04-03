# Generated by Django 2.1.3 on 2019-02-20 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commands',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('command', models.CharField(max_length=10)),
                ('paramters', models.CharField(max_length=10)),
                ('alreadyExists', models.BooleanField()),
                ('argumentsProv', models.CharField(max_length=20)),
                ('isPiped', models.BooleanField()),
                ('userid', models.IntegerField()),
                ('isAlais', models.BooleanField()),
                ('orginal', models.CharField(max_length=10)),
                ('pastaComments', models.CharField(max_length=100)),
                ('isRoot', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='ServerReply',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('replyText', models.CharField(max_length=100)),
                ('alreadyExists', models.BooleanField()),
            ],
        ),
    ]