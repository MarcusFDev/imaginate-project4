# Generated by Django 4.2.16 on 2024-10-13 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='excerpt',
            field=models.TextField(),
        ),
    ]
