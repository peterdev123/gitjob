# Generated by Django 5.1.1 on 2024-10-25 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_remove_resume_filename'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='filename',
            field=models.CharField(default='Unnamed Resume.pdf', max_length=100),
        ),
    ]
