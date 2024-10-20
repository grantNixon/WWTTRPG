from django.urls import path
from . import views


urlpatterns = [
    path('', views.test_view, name="home_page"),
    path("getting_started", views.getting_started, name="getting_started"),
    
]
