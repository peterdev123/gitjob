from django.db import models
from django.conf import settings 
import shortuuid

# Create your models here.
class ChatGroup(models.Model):
    group_name = models.CharField(max_length=128, unique=True, default=shortuuid.uuid)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='chat_groups', blank=True)
    is_private = models.BooleanField(default=False)

    def __str__(self):
        return self.group_name
class SearchedUsers(models.Model):
    current_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    recent_searched_users = models.JSONField(default=list, blank=True)

    def add_recent_user(self, username):
        if username in self.recent_searched_users:
            self.recent_searched_users.remove(username)

        self.recent_searched_users.insert(0, username)

        self.recent_searched_users = self.recent_searched_users[:15]

        self.save()

    def __str__(self):
        return self.username
    
class GroupMessage(models.Model):
    group = models.ForeignKey(ChatGroup, related_name='chat_messages', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author.username} : {self.body}'
    
    class Meta:
        ordering = ['-created']