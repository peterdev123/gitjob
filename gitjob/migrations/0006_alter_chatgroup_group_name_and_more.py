# Generated by Django 5.1.3 on 2024-11-11 11:31

import django.db.models.deletion
import shortuuid.main
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gitjob', '0005_alter_chatgroup_group_name_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatgroup',
            name='group_name',
            field=models.CharField(default=shortuuid.main.ShortUUID.uuid, max_length=128, unique=True),
        ),
        migrations.AlterField(
            model_name='searchedusers',
            name='current_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='searchedusers',
            name='recent_searched_users',
        ),
        migrations.AddField(
            model_name='searchedusers',
            name='recent_searched_users',
            field=models.JSONField(blank=True, default=list),
        ),
    ]
