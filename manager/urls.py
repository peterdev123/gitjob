from django.urls import path
from . import views

urlpatterns = [
    path('post_jobs/', views.post_jobs, name="post_jobs")
]