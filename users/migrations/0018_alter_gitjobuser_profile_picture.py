# Generated by Django 5.1.1 on 2024-10-25 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_gitjobuser_profile_picture_alter_resume_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gitjobuser',
            name='profile_picture',
            field=models.ImageField(default='static/images/default_profile_picture.png', upload_to=''),
        ),
    ]
