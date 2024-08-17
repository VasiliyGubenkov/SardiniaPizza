from django.urls import path
from . import views_web, views_api

app_name = 'main'

urlpatterns = [
    path('', views_web.start, name='start'),
    path('index/', views_web.index, name='index'),
    path('about/', views_web.about, name='about'),
]