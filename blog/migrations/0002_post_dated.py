# Generated by Django 4.2.1 on 2023-06-09 06:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='dated',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
