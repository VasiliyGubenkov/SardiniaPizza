from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *


class PizzaView(APIView):
    def get(self, request, pk=None):
        # Получаем query parameters из запроса
        query_params = request.query_params

        # Проверяем условия
        if pk is None and not query_params:
            all_pizzas = Pizza.objects.all()
            all_pizzas_serializered = PizzaSerializer(all_pizzas, many=True)
            return Response(all_pizzas_serializered.data, status=200)

        elif pk is not None and not query_params:
            # Если есть только pk
            return Response({"message": f"Запрос с pk: {pk}"}, status=200)

        elif pk is None and query_params:
            # Если есть только query parameters
            return Response({"message": f"Запрос с query parameters: {query_params}"}, status=200)

        else:
            # Если есть и pk, и query parameters
            return Response({"message": f"Запрос с pk: {pk} и query parameters: {query_params}"}, status=200)

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