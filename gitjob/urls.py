from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.hero, name=""),
    path('users/', include('users.urls')),
]