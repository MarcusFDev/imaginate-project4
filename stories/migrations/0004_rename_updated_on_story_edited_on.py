# Generated by Django 4.2.15 on 2024-08-29 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0003_alter_story_options_story_excerpt_story_updated_on_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='story',
            old_name='updated_on',
            new_name='edited_on',
        ),
    ]
