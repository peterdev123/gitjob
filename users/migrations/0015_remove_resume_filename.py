# Generated by Django 5.1.1 on 2024-10-25 06:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_alter_resume_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resume',
            name='filename',
        ),
    ]
