from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *


class PizzaView(APIView):
    def get(self, request):
        # Получаем query parameters из запроса
        query_params = request.query_params

        # Проверяем условия
        if not query_params:
            all_pizzas = Pizza.objects.all()
            all_pizzas_serializered = PizzaSerializer(all_pizzas, many=True)
            return Response(all_pizzas_serializered.data, status=status.HTTP_200_OK)

        else:
            # Если есть query parameters
            # Фильтруем по каждому из возможных параметров
            pizzas = Pizza.objects.all()
            if 'name' in query_params:
                pizzas = pizzas.filter(name=query_params['name'])
            if 'size' in query_params:
                pizzas = pizzas.filter(size=query_params['size'])
            if 'price' in query_params:
                pizzas = pizzas.filter(price=query_params['price'])
            if 'discount' in query_params:
                pizzas = pizzas.filter(discount=query_params['discount'])
            if 'category_of_pizza' in query_params:
                pizzas = pizzas.filter(category_of_pizza=query_params['category_of_pizza'])
            if 'slug' in query_params:
                pizzas = pizzas.filter(slug=query_params['slug'])

            # Сериализуем отфильтрованные объекты
            pizzas_serializered = PizzaSerializer(pizzas, many=True)

            return Response(pizzas_serializered.data, status=status.HTTP_200_OK)


    def post(self, request, pk):
        pass
    def put(self, request, pk): #метод для полной замены данных обьекта.
        pass
    def delete(self, request, pk):
        pass
    def patch(self, request, pk): #метод для частичной замены, только некоторых, данных обьекта.
        pass


class DrinkView(APIView):
    def get(self, request, pk):
        pass
    def post(self, request, pk):
        pass
    def put(self, request, pk): #метод для полной замены данных обьекта.
        pass
    def delete(self, request, pk):
        pass
    def patch(self, request, pk): #метод для частичной замены, только некоторых, данных обьекта.
        pass


class UserView(APIView):
    def get(self, request, pk):
        pass
    def post(self, request, pk):
        pass
    def put(self, request, pk): #метод для полной замены данных обьекта.
        pass
    def delete(self, request, pk):
        pass
    def patch(self, request, pk): #метод для частичной замены, только некоторых, данных обьекта.
        pass

class BasketView(APIView):
    def get(self, request, pk):
        pass
    def post(self, request, pk):
        pass
    def put(self, request, pk): #метод для полной замены данных обьекта.
        pass
    def delete(self, request, pk):
        pass
    def patch(self, request, pk): #метод для частичной замены, только некоторых, данных обьекта.
        pass


class OrderView(APIView):
    def get(self, request, pk):
        pass
    def post(self, request, pk):
        pass
    def put(self, request, pk): #метод для полной замены данных обьекта.
        pass
    def delete(self, request, pk):
        pass
    def patch(self, request, pk): #метод для частичной замены, только некоторых, данных обьекта.
        pass