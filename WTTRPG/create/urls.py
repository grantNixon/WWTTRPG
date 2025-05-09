from django.urls import path
from . import views
from .views import *

app_name = 'create'

urlpatterns = [
    path('', views.create_view),
    path('homebrew/', views.homebrew_view),
    path('quickstart_create/',QSCharCreator.as_view(), name='qscc'),
    path('character_detail/<int:pk>', CharacterSheet.as_view(), name="character_sheet"),
    path('update_skills', views.update_skills, name="update_skills"),
    path('retrieve_skills', views.retrieve_skills, name="retrieve_skills"),
    path('character_list/',CharacterListView.as_view(), name="character_list"),
    path('test_packet/', views.download_testpacket, name = 'test_packet'),
    path('oneshot/', views.download_oneshot, name = 'oneshot'),
    path('user_profile/', UserProfileView.as_view(), name= 'user_profile') 
]
