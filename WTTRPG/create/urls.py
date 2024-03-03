from django.urls import path
from . import views
from .views import *

app_name = 'create'

urlpatterns = [
    path('', views.create_view),
    path('homebrew/', views.homebrew_view),
    path('quickstart_create/',QSCharCreator.as_view(), name='qscc')
]
