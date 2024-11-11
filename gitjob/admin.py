from django.contrib import admin
from .models import ChatGroup, GroupMessage, SearchedUsers

# Register your models here.
admin.site.register(ChatGroup)
admin.site.register(GroupMessage)
admin.site.register(SearchedUsers)