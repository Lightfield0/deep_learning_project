from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('introduction/', views.introduction, name="introduction"),
    path('how-it-works/', views.how_it_works, name="how-it-works"),
    path('types-of-nn/', views.types_of_nn, name="types-of-nn"),
    path('about-us/', views.about_us, name="about-us"),
    path('deep-learning-projects/', views.deep_learning_projects, name="deep-learning-projects"),
    path('contact/', views.contact, name="contact"),
]