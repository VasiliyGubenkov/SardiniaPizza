from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views_web, views_api, views_api_GenericAPIViewMethod, views_api_LogicMethod, views_api_DecoratorMethod, views_api_ModelMethod


# Создание экземпляра маршрутизатора и регистрация вьюшек в нём(для модел-метода)
# router = DefaultRouter()
# router.register(r'pizza', views_api_ModelMethod.PizzaViewSet, basename='pizza')
# router.register(r'drink', views_api_ModelMethod.DrinkViewSet, basename='drink')
# router.register(r'user', views_api_ModelMethod.UserViewSet, basename='user')
# router.register(r'basket', views_api_ModelMethod.BasketViewSet, basename='basket')
# router.register(r'order', views_api_ModelMethod.OrderViewSet, basename='order')

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

    # Блок путей для вьюшек с дженериками
    # path('api/pizza/', views_api_GenericAPIViewMethod.PizzaListCreateView.as_view(), name='pizza-list-create'),
    # path('api/pizza/<int:pk>/', views_api_GenericAPIViewMethod.PizzaRetrieveUpdateDestroyView.as_view(), name='pizza-retrieve-update-destroy'),
    # path('api/drink/', views_api_GenericAPIViewMethod.DrinkListCreateView.as_view(), name='drink-list-create'),
    # path('api/drink/<int:pk>/', views_api_GenericAPIViewMethod.DrinkRetrieveUpdateDestroyView.as_view(), name='drink-retrieve-update-destroy'),
    # path('api/user/', views_api_GenericAPIViewMethod.UserListCreateView.as_view(), name='user-list-create'),
    # path('api/user/<int:pk>/', views_api_GenericAPIViewMethod.UserRetrieveUpdateDestroyView.as_view(), name='user-retrieve-update-destroy'),
    # path('api/basket/', views_api_GenericAPIViewMethod.BasketListCreateView.as_view(), name='basket-list-create'),
    # path('api/basket/<int:pk>/', views_api_GenericAPIViewMethod.BasketRetrieveUpdateDestroyView.as_view(), name='basket-retrieve-update-destroy'),
    # path('api/order/', views_api_GenericAPIViewMethod.OrderListCreateView.as_view(), name='order-list-create'),
    # path('api/order/<int:pk>/', views_api_GenericAPIViewMethod.OrderRetrieveUpdateDestroyView.as_view(), name='order-retrieve-update-destroy'),

    # Блок путей для вьюшек с логическим ветвлением
    # path('api/pizza/', views_api_LogicMethod.PizzaView, name='pizza-list'),
    # path('api/drink/', views_api_LogicMethod.DrinkView, name='drink-list'),
    # path('api/user/', views_api_LogicMethod.UserView, name='user-list'),
    # path('api/basket/', views_api_LogicMethod.BasketView, name='basket-list'),
    # path('api/order/', views_api_LogicMethod.OrderView, name='order-list'),

    # Блок путей для вьюшек с декораторами
    # path('api/pizza/', views_api_DecoratorMethod.PizzaView, name='pizza-list'),
    # path('api/drink/', views_api_DecoratorMethod.DrinkView, name='drink-list'),
    # path('api/user/', views_api_DecoratorMethod.UserView, name='user-list'),
    # path('api/basket/', views_api_DecoratorMethod.BasketView, name='basket-list'),
    # path('api/order/', views_api_DecoratorMethod.OrderView, name='order-list'),

    # Блок путь для вьюшек модел-вью-сет
    # path('api/', include(router.urls)),

]