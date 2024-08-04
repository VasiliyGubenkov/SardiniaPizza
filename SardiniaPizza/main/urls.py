from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.start, name='start'),
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
]