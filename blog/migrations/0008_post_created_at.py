# Generated by Django 4.2.1 on 2023-06-12 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_remove_post_active_post_is_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='created_at',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]