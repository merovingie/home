# Generated by Django 2.1.3 on 2019-02-20 22:40

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('djangoendpoint', '0002_auto_20190220_2233'),
    ]

    operations = [
        migrations.AddField(
            model_name='commands',
            name='UserShell',
            field=models.ForeignKey(blank=True, default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to='djangoendpoint.UserShell'),
            preserve_default=False,
        ),
    ]
