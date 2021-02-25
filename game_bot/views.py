from django.shortcuts import render
from .models import GameScores
from django.views.generic.list import ListView


class ScoreListView(ListView):
    model = GameScores
    template_name = 'scores_list.html'
    context_object_name = 'scores_list'