from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Pizza, Drink, User, Basket, Order
from .serializers import PizzaSerializer, DrinkSerializer, UserSerializer, BasketSerializer, OrderSerializer

class PizzaViewSet(viewsets.ModelViewSet):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['id', 'name', 'size', 'price', 'discount', 'category_of_pizza', 'slug']
    ordering_fields = '__all__'
    ordering = ['name']

class DrinkViewSet(viewsets.ModelViewSet):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['id', 'name', 'size', 'price', 'discount', 'category_of_drinks', 'slug']
    ordering_fields = '__all__'
    ordering = ['name']

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['user_login', 'name', 'surname', 'email', 'phone', 'slug']
    ordering_fields = '__all__'
    ordering = ['name']

class BasketViewSet(viewsets.ModelViewSet):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['user', 'content_type', 'object_id', 'price_of_good', 'quantity_of_good', 'slug']
    ordering_fields = '__all__'
    ordering = ['user']

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['user', 'address_of_delivery', 'content_of_order', 'amount', 'status_of_payment', 'status_of_delivery', 'slug']
    ordering_fields = '__all__'
    ordering = ['user']
