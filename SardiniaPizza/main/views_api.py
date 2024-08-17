from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class PizzaView(APIView):
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