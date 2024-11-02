from django.urls import path
from . import views

urlpatterns = [
    path('job_posting/<int:id>', views.job_posting_view, name='job_posting')
]