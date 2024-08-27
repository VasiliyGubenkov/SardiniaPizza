from django.urls import path
from . import views_web, views_api, views_api_GenericAPIView, views_api_LogicMethod, views_api_DecoratorMethod


app_name = 'main'

urlpatterns = [
    path('', views_web.start, name='start'),
    path('index/', views_web.index, name='index'),
    path('about/', views_web.about, name='about'),
    #path('api/pizza/', views_api.PizzaView.as_view(), name='pizza'),
    #path('api/drink/', views_api.DrinkView.as_view(), name='drink'),
    #path('api/user/', views_api.UserView.as_view(), name='user'),
    #path('api/basket/', views_api.BasketView.as_view(), name='basket'),
    #path('api/order/', views_api.OrderView.as_view(), name='order'),
    path('api/pizza/', views_api_GenericAPIView.PizzaView.as_view(), name='pizza'),
    path('api/drink/', views_api_GenericAPIView.DrinkView.as_view(), name='drink'),
    path('api/user/', views_api_GenericAPIView.UserView.as_view(), name='user'),
    path('api/basket/', views_api_GenericAPIView.BasketView.as_view(), name='basket'),
    path('api/order/', views_api_GenericAPIView.OrderView.as_view(), name='order'),
]