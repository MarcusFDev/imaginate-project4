# Generated by Django 4.2.15 on 2024-08-29 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='story',
            name='is_hidden',
        ),
        migrations.AddField(
            model_name='story',
            name='is_private',
            field=models.BooleanField(default=True),
        ),
    ]
