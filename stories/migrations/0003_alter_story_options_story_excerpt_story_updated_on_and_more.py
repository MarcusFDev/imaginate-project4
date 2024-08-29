# Generated by Django 4.2.15 on 2024-08-29 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0002_remove_story_is_hidden_story_is_private'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='story',
            options={'ordering': ['-created_on']},
        ),
        migrations.AddField(
            model_name='story',
            name='excerpt',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='story',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='story',
            name='upvotes',
            field=models.IntegerField(default=0),
        ),
    ]
