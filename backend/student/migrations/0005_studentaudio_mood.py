# Generated by Django 4.1 on 2022-08-26 09:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_feeling'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentaudio',
            name='mood',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
