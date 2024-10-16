# Generated by Django 4.2.16 on 2024-10-16 10:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userprofile_delete_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsletterSignup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.EmailField(max_length=254, unique=True)),
                ('signup_data', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_active', models.BooleanField(default=True, null=True)),
            ],
        ),
    ]
