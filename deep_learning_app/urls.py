from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('introduction/', views.introduction, name="introduction"),
    path('types-of-nn/', views.types_of_nn, name="types-of-nn")
]