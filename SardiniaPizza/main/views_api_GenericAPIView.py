from rest_framework import generics
from .models import Pizza, Drink
from .serializers import PizzaSerializer, DrinkSerializer

# Pizza views
class PizzaListCreateView(generics.ListCreateAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        params = self.request.query_params
        for key in params:
            if key in ['id', 'name', 'size', 'price', 'discount', 'category_of_pizza', 'slug']:
                queryset = queryset.filter(**{key: params[key]})
        return queryset

class PizzaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer

    def get_object(self):
        params = self.request.query_params
        if params:
            queryset = self.queryset
            for key in params:
                if key in ['id', 'name', 'size', 'price', 'discount', 'category_of_pizza', 'slug']:
                    queryset = queryset.filter(**{key: params[key]})
            if queryset.exists():
                return queryset.first()
        return super().get_object()

# Drink views
class DrinkListCreateView(generics.ListCreateAPIView):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        params = self.request.query_params
        for key in params:
            if key in ['id', 'name', 'size', 'price', 'discount', 'category_of_drinks', 'slug']:
                queryset = queryset.filter(**{key: params[key]})
        return queryset

class DrinkRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer

    def get_object(self):
        params = self.request.query_params
        if params:
            queryset = self.queryset
            for key in params:
                if key in ['id', 'name', 'size', 'price', 'discount', 'category_of_drinks', 'slug']:
                    queryset = queryset.filter(**{key: params[key]})
            if queryset.exists():
                return queryset.first()
        return super().get_object()

# User views
class UserListCreateView(generics.ListCreateAPIView):
    pass

class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    pass

# Basket views
class BasketListCreateView(generics.ListCreateAPIView):
    pass

class BasketRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    pass

# Order views
class OrderListCreateView(generics.ListCreateAPIView):
    pass

class OrderRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    pass

