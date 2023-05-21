from django.shortcuts import render, redirect

from .Services.Tasks import Tasks
from .models import Daylies, Player, Quests
from django.http import HttpRequest


# Create your views here.

def base(request: HttpRequest):
    tasks: Tasks = Tasks(request)
    return render(request, 'main/base.html', tasks.update())