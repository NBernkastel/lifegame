from django.templatetags.static import static
from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('', views.base, name='base')
]
