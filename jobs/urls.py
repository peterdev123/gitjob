from django.urls import path
from . import views
import manager.views

urlpatterns = [
    path('job_posting/<int:id>', views.job_posting_view, name='job_posting'),
    path('job_post/', views.job_post, name='job_post'),
    path('edit/<int:post_id>/', manager.views.edit_job_post, name='edit_job_post'),
    path('delete/<int:post_id>/', views.delete_job_post, name='delete_job_post'),
    path('application_history', views.job_application_history_view, name='job_application_history')
]