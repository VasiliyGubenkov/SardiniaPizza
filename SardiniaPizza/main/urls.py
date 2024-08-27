from django.urls import path
from . import views_web, views_api, views_api_GenericAPIView, views_api_LogicMethod, views_api_DecoratorMethod


app_name = 'main'

urlpatterns = [
    path('', views_web.start, name='start'),

    #Блок путей для моих любимых апи-вьюшек
    path('index/', views_web.index, name='index'),
    path('about/', views_web.about, name='about'),
    path('api/pizza/', views_api.PizzaView.as_view(), name='pizza'),
    path('api/drink/', views_api.DrinkView.as_view(), name='drink'),
    path('api/user/', views_api.UserView.as_view(), name='user'),
    path('api/basket/', views_api.BasketView.as_view(), name='basket'),
    path('api/order/', views_api.OrderView.as_view(), name='order'),

    #Блок путей для вьюшек с дженериками
    #path('pizza/', views_api_GenericAPIView.PizzaListCreateView.as_view(), name='pizza-list-create'),
    #path('pizza/<int:pk>/', views_api_GenericAPIView.PizzaRetrieveUpdateDestroyView.as_view(), name='pizza-retrieve-update-destroy'),
    #path('drink/', views_api_GenericAPIView.DrinkListCreateView.as_view(), name='drink-list-create'),
    #path('drink/<int:pk>/', views_api_GenericAPIView.DrinkRetrieveUpdateDestroyView.as_view(), name='drink-retrieve-update-destroy'),
    #path('user/', views_api_GenericAPIView.UserListCreateView.as_view(), name='user-list-create'),
    #path('user/<int:pk>/', views_api_GenericAPIView.UserRetrieveUpdateDestroyView.as_view(), name='user-retrieve-update-destroy'),
    #path('basket/', views_api_GenericAPIView.BasketListCreateView.as_view(), name='basket-list-create'),
    #path('basket/<int:pk>/', views_api_GenericAPIView.BasketRetrieveUpdateDestroyView.as_view(), name='basket-retrieve-update-destroy'),
    #path('order/', views_api_GenericAPIView.OrderListCreateView.as_view(), name='order-list-create'),
    #path('order/<int:pk>/', views_api_GenericAPIView.OrderRetrieveUpdateDestroyView.as_view(), name='order-retrieve-update-destroy'),

    #Блок путей для вьюшек с логическим ветвлением


]