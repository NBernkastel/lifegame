from django.contrib import admin

from . import models


# Register your models here.

@admin.register(models.Player)
class PlayerModel(admin.ModelAdmin):
    list_display = ['user', 'user_hp', 'user_lvl']


@admin.register(models.Daylies)
class DayliesModel(admin.ModelAdmin):
    list_display = ['Player', 'text', 'count', 'series', 'is_ready']


@admin.register(models.Quests)
class QuestsModel(admin.ModelAdmin):
    list_display = ['Player', 'text', 'is_ready']

@admin.register(models.Habits)
class HabitsModel(admin.ModelAdmin):
    list_display = ['Player', 'text', 'count', 'serial']
