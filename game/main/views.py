from django.shortcuts import render, redirect

from .models import Daylies, Player
from django.http import HttpRequest


# Create your views here.

def base(request: HttpRequest):
    daylies = Daylies.objects.all()
    if request.method == 'POST':
        print(request.POST.dict())
        new = Daylies(text=request.POST.dict()['new'], Player=Player.objects.get(user=request.user))
        new.save()
        return redirect('/')
    return render(request, 'main/base.html', {'daylies': daylies})
