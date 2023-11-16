from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('introduction/', views.introduction, name="introduction"),
    path('types-of-nn/', views.types_of_nn, name="types-of-nn"),
    path('about-us/', views.about_us, name="about-us")
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)