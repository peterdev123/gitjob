# Generated by Django 5.1.1 on 2024-11-19 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0024_gitjobuser_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='last_updated',
            field=models.DateField(blank=True, null=True),
        ),
    ]