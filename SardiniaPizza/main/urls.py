from django.urls import path
from . import views_web, views_api

app_name = 'main'

urlpatterns = [
    path('', views_web.start, name='start'),
    path('index/', views_web.index, name='index'),
    path('about/', views_web.about, name='about'),
    path('api/pizza/', views_api.PizzaView.as_view(), name='pizza'),
    path('api/drink/', views_api.DrinkView.as_view(), name='drink'),
    path('api/user/', views_api.UserView.as_view(), name='user'),
    path('api/basket/', views_api.BasketView.as_view(), name='basket'),
    path('api/order/', views_api.OrderView.as_view(), name='order'),
]