from django.contrib import admin
from django.urls import path
from .views import ScoreListView


app_name = 'game_bot'

urlpatterns = [
    path('', ScoreListView.as_view(), name='score_list')
]