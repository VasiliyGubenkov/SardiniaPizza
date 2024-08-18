
from django.contrib import admin
from django.urls import path, include
from main.views_web import *
from main.views_api import *

from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace='main')),
    #path('', views.index, name='home'),
]
