# Generated by Django 5.1.1 on 2024-10-16 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_gitjobuser_about_gitjobuser_address_gitjobuser_job_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gitjobuser',
            old_name='address',
            new_name='home_address',
        ),
    ]
