"""
URL configuration for the Motion Workspace Django project.
This file connects website addresses to the correct view functions.
"""

from django.contrib import admin
from django.urls import path
from app import views


urlpatterns = [
    # Home page
    path('', views.home, name='home'),

    # Main project pages
    path('dashboard/', views.dashboard, name='dashboard'),
    path('notes/', views.notes, name='notes'),
    path('calendar/', views.calendar, name='calendar'),
    path('reminders/', views.reminders, name='reminders'),

    # User pages
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),

    # Default informational pages
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    # Django admin page
    path('admin/', admin.site.urls),
]