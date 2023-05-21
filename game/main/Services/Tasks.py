from django.http import HttpRequest
from django.shortcuts import redirect, render

from ..models import Daylies, Quests, Habits, Player


class Tasks:
    def __init__(self, request: HttpRequest):
        self.__daylies: list[Daylies] = Daylies.objects.all()
        self.__quests: list[Quests] = Quests.objects.all()
        self.__habits: list[Habits] = Habits.objects.all()
        self.__request = request

    def addEntry(self):
        if self.__request.POST.get('daylies'):
            Daylies.objects.create(text=self.__request.POST.get('daylies'),
                                   Player=Player.objects.get(user=self.__request.user))
        if self.__request.POST.get('quests'):
            Quests.objects.create(Player=Player.objects.get(user=self.__request.user),
                                  text=self.__request.POST.get('quests'))
        if self.__request.POST.get('habits'):
            Habits.objects.create(Player=Player.objects.get(user=self.__request.user),
                                  text=self.__request.POST.get('habits'))

    def update(self) -> dict[str, list[Daylies, Quests, Habits]]:
        if self.__request.method == 'POST':
            self.addEntry()
            for i in self.__daylies:
                if str(i.id) in self.__request.POST.getlist('dayItem[]'):
                    i.is_ready = True
                else:
                    i.is_ready = False
                i.save()
            for i in self.__quests:
                if str(i.id) in self.__request.POST.getlist('questsItem[]'):
                    i.is_ready = True
                else:
                    i.is_ready = False
                i.save()
            for i in self.__habits:
                if str(i.id) in self.__request.POST.getlist('habitsItem[]'):
                    i.count += 1
                i.save()

        return {'daylies': self.__daylies, 'quests': self.__quests, 'habits': self.__habits}
