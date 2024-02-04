from django.urls import path
from . import views

urlpatterns = [
    path('', views.guide_view),
    path('mg_purchase/', views.mg_purchase_view)
]
