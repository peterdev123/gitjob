from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.hero, name=""),
    path('home/', views.homepage, name='home'),
    path('messages/', views.messages, name='messages'),
    path('contactus/', views.contactus, name='contactus'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('users/', include('users.urls')),
    path('manager/', include('manager.urls')),
    # path('user_messages/', include('user_messages.urls')),
]