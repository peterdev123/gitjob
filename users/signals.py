import os
from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Resume

@receiver(post_delete, sender=Resume)
def delete_file_on_model_delete(sender, instance, **kwargs):
    if instance.file:
        if os.path.isfile(instance.file.path):
            os.remove(instance.file.path)