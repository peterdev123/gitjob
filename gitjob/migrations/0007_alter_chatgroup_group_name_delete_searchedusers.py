# Generated by Django 5.1.3 on 2024-11-12 09:23

import shortuuid.main
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gitjob', '0006_alter_chatgroup_group_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatgroup',
            name='group_name',
            field=models.CharField(default=shortuuid.main.ShortUUID.uuid, max_length=128, unique=True),
        ),
        migrations.DeleteModel(
            name='SearchedUsers',
        ),
    ]
