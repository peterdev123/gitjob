# Generated by Django 5.1.1 on 2024-11-10 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0023_alter_gitjobuser_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='gitjobuser',
            name='country',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]