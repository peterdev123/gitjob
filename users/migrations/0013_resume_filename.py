# Generated by Django 5.1.1 on 2024-10-24 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_remove_gitjobuser_user_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='filename',
            field=models.CharField(default='Unnamed Resume.pdf', max_length=100),
        ),
    ]
