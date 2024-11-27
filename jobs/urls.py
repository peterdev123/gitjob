from django.urls import path
from . import views

urlpatterns = [
    path('job_posting/<int:id>', views.job_posting_view, name='job_posting'),
    path('job_post/', views.job_post, name='job_post'),
    path('application_history', views.job_application_history_view, name='job_application_history')
]