from django.contrib import admin
from django.urls import path, include
from .views import UserListView

app_name = 'users'

urlpatterns = [
    path('', UserListView.as_view(), name='users_list'),
]