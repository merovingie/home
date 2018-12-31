# Generated by Django 2.1.3 on 2018-12-13 23:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='boxDisplayView',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cassettes', models.IntegerField(default=0)),
                ('contianers', models.IntegerField(default=0)),
                ('DID_num', models.BigIntegerField(default=0)),
                ('DID_type', models.CharField(choices=[('ST', 'Stat'), ('OR', 'Oral'), ('IH', 'In House'), ('OR', 'Orange Dot')], max_length=30)),
                ('DID_comments', models.CharField(choices=[('PAS', 'Plasma Stain'), ('RO', 'RO Something')], max_length=30)),
                ('DID_date_created', models.DateTimeField(auto_now_add=True)),
                ('author_box', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Entrynew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('time', models.TimeField(auto_now_add=True)),
                ('duration', models.TimeField()),
                ('box_number', models.IntegerField(default=0)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('authQuest', models.CharField(max_length=10)),
                ('message_field', models.CharField(max_length=150)),
                ('email_field', models.EmailField(max_length=254)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('Box_type', models.CharField(max_length=6)),
                ('cassettes_num', models.IntegerField(default=0)),
                ('container_num', models.IntegerField(default=0)),
                ('reqtotal_num', models.IntegerField(default=0)),
                ('starting_DIDSTR', models.CharField(max_length=11)),
                ('starting_DID', models.BigIntegerField(default=0)),
                ('ending_DID', models.BigIntegerField(default=0)),
                ('problem_flag', models.CharField(max_length=15)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]