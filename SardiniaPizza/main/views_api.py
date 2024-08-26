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
            if 'id' in query_params:
                pizzas = pizzas.filter(id=int(query_params['id']))
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


    def post(self, request):
        serializer = PizzaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        # Получаем query parameters из запроса
        query_params = request.query_params

        if not query_params:
            return Response({"error": "Нет параметров для поиска нужной пиццы, для последующего обновления"},
                            status=status.HTTP_400_BAD_REQUEST)

        # Фильтруем пиццы по всем возможным query parameters
        object_to_update = Pizza.objects.all()
        if 'id' in query_params:
            object_to_update = object_to_update.filter(id=int(query_params['id']))
        if 'name' in query_params:
            object_to_update = object_to_update.filter(name=query_params['name'])
        if 'size' in query_params:
            object_to_update = object_to_update.filter(size=query_params['size'])
        if 'price' in query_params:
            object_to_update = object_to_update.filter(price=query_params['price'])
        if 'discount' in query_params:
            object_to_update = object_to_update.filter(discount=query_params['discount'])
        if 'category_of_pizza' in query_params:
            object_to_update = object_to_update.filter(category_of_pizza=query_params['category_of_pizza'])
        if 'slug' in query_params:
            object_to_update = object_to_update.filter(slug=query_params['slug'])

        # Проверяем, что объект существует
        if object_to_update.exists():
            # Берём первый найденный объект (например, если найдено несколько по фильтру)
            pizza = object_to_update.first()
            serializer = PizzaSerializer(pizza, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "Пицца с такими параметрами не найдена"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request):
        # Получаем query parameters из запроса
        query_params = request.query_params
        if not query_params:
            return Response({"error": "Нет параметров для поиска нужной пиццы, для последующего удаления"}, status=status.HTTP_400_BAD_REQUEST)
        else:
        # Фильтруем пиццы по всем возможным query parameters
            object_to_delete = Pizza.objects.all()
            if 'id' in query_params:
                object_to_delete = object_to_delete.filter(id=int(query_params['id']))
            if 'name' in query_params:
                object_to_delete = object_to_delete.filter(name=query_params['name'])
            if 'size' in query_params:
                object_to_delete = object_to_delete.filter(size=query_params['size'])
            if 'price' in query_params:
                object_to_delete = object_to_delete.filter(price=query_params['price'])
            if 'discount' in query_params:
                object_to_delete = object_to_delete.filter(discount=query_params['discount'])
            if 'category_of_pizza' in query_params:
                object_to_delete = object_to_delete.filter(category_of_pizza=query_params['category_of_pizza'])
            if 'slug' in query_params:
                object_to_delete = object_to_delete.filter(slug=query_params['slug'])
            # Удаляем все найденные пиццы
            try:
                object_to_delete.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except:
                return Response({"error": "Не удалось удалить пиццу с такими параметрами поиска"}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request):
        # Получаем query parameters из запроса
        query_params = request.query_params

        if not query_params:
            return Response({"error": "Нет параметров для поиска нужной пиццы, для последующего обновления"},
                            status=status.HTTP_400_BAD_REQUEST)

        # Фильтруем пиццы по всем возможным query parameters
        object_to_update = Pizza.objects.all()
        if 'id' in query_params:
            object_to_update = object_to_update.filter(id=int(query_params['id']))
        if 'name' in query_params:
            object_to_update = object_to_update.filter(name=query_params['name'])
        if 'size' in query_params:
            object_to_update = object_to_update.filter(size=query_params['size'])
        if 'price' in query_params:
            object_to_update = object_to_update.filter(price=query_params['price'])
        if 'discount' in query_params:
            object_to_update = object_to_update.filter(discount=query_params['discount'])
        if 'category_of_pizza' in query_params:
            object_to_update = object_to_update.filter(category_of_pizza=query_params['category_of_pizza'])
        if 'slug' in query_params:
            object_to_update = object_to_update.filter(slug=query_params['slug'])

        # Проверяем, что объект существует
        if object_to_update.exists():
            pizza = object_to_update.first()
            serializer = PizzaSerializer(pizza, data=request.data,
                                         partial=True)  # partial=True для частичного обновления
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "Пицца с такими параметрами не найдена"}, status=status.HTTP_404_NOT_FOUND)


class DrinkView(APIView):
    def get(self, request):
        # Получаем query parameters из запроса
        query_params = request.query_params

        # Проверяем условия
        if not query_params:
            all_drinks = Drink.objects.all()
            all_drinks_serializered = DrinkSerializer(all_drinks, many=True)
            return Response(all_drinks_serializered.data, status=status.HTTP_200_OK)

        else:
            # Если есть query parameters
            # Фильтруем напитки по каждому из возможных параметров
            drinks = Drink.objects.all()
            if 'id' in query_params:
                drinks = drinks.filter(id=int(query_params['id']))
            if 'name' in query_params:
                drinks = drinks.filter(name=query_params['name'])
            if 'size' in query_params:
                drinks = drinks.filter(size=query_params['size'])
            if 'price' in query_params:
                drinks = drinks.filter(price=query_params['price'])
            if 'discount' in query_params:
                drinks = drinks.filter(discount=query_params['discount'])
            if 'category_of_drinks' in query_params:
                drinks = drinks.filter(category_of_drinks=query_params['category_of_drinks'])
            if 'slug' in query_params:
                drinks = drinks.filter(slug=query_params['slug'])

            # Сериализуем отфильтрованные объекты
            drinks_serializered = DrinkSerializer(drinks, many=True)

            return Response(drinks_serializered.data, status=status.HTTP_200_OK)


    def post(self, request):
        serializer = DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        # Получаем query parameters из запроса
        query_params = request.query_params

        if not query_params:
            return Response({"error": "Нет параметров для поиска нужного напитка, для последующего обновления"},
                            status=status.HTTP_400_BAD_REQUEST)

        # Фильтруем напитки по всем возможным query parameters
        object_to_update = Drink.objects.all()
        if 'id' in query_params:
            object_to_update = object_to_update.filter(id=int(query_params['id']))
        if 'name' in query_params:
            object_to_update = object_to_update.filter(name=query_params['name'])
        if 'size' in query_params:
            object_to_update = object_to_update.filter(size=query_params['size'])
        if 'price' in query_params:
            object_to_update = object_to_update.filter(price=query_params['price'])
        if 'discount' in query_params:
            object_to_update = object_to_update.filter(discount=query_params['discount'])
        if 'category_of_drinks' in query_params:
            object_to_update = object_to_update.filter(category_of_pizza=query_params['category_of_drinks'])
        if 'slug' in query_params:
            object_to_update = object_to_update.filter(slug=query_params['slug'])

        # Проверяем, что объект существует
        if object_to_update.exists():
            # Берём первый найденный объект (например, если найдено несколько по фильтру)
            drink = object_to_update.first()
            serializer = DrinkSerializer(drink, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "Напиток с такими параметрами не найден"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request):
        # Получаем query parameters из запроса
        query_params = request.query_params
        if not query_params:
            return Response({"error": "Нет параметров для поиска нужного напитка, для последующего удаления"}, status=status.HTTP_400_BAD_REQUEST)
        else:
        # Фильтруем напитки по всем возможным query parameters
            object_to_delete = Drink.objects.all()
            if 'id' in query_params:
                object_to_delete = object_to_delete.filter(id=int(query_params['id']))
            if 'name' in query_params:
                object_to_delete = object_to_delete.filter(name=query_params['name'])
            if 'size' in query_params:
                object_to_delete = object_to_delete.filter(size=query_params['size'])
            if 'price' in query_params:
                object_to_delete = object_to_delete.filter(price=query_params['price'])
            if 'discount' in query_params:
                object_to_delete = object_to_delete.filter(discount=query_params['discount'])
            if 'category_of_drink' in query_params:
                object_to_delete = object_to_delete.filter(category_of_pizza=query_params['category_of_drink'])
            if 'slug' in query_params:
                object_to_delete = object_to_delete.filter(slug=query_params['slug'])
            # Удаляем все найденные напитки
            try:
                object_to_delete.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except:
                return Response({"error": "Не удалось удалить напитки с такими параметрами поиска"}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request):
        # Получаем query parameters из запроса
        query_params = request.query_params

        if not query_params:
            return Response({"error": "Нет параметров для поиска нужного напитка, для последующего обновления"},
                            status=status.HTTP_400_BAD_REQUEST)

        # Фильтруем напитки по всем возможным query parameters
        object_to_update = Drink.objects.all()
        if 'id' in query_params:
            object_to_update = object_to_update.filter(id=int(query_params['id']))
        if 'name' in query_params:
            object_to_update = object_to_update.filter(name=query_params['name'])
        if 'size' in query_params:
            object_to_update = object_to_update.filter(size=query_params['size'])
        if 'price' in query_params:
            object_to_update = object_to_update.filter(price=query_params['price'])
        if 'discount' in query_params:
            object_to_update = object_to_update.filter(discount=query_params['discount'])
        if 'category_of_drink' in query_params:
            object_to_update = object_to_update.filter(category_of_pizza=query_params['category_of_drink'])
        if 'slug' in query_params:
            object_to_update = object_to_update.filter(slug=query_params['slug'])

        # Проверяем, что объект существует
        if object_to_update.exists():
            drink = object_to_update.first()
            serializer = DrinkSerializer(drink, data=request.data,
                                         partial=True)  # partial=True для частичного обновления
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "Напиток с такими параметрами не найден"}, status=status.HTTP_404_NOT_FOUND)


class UserView(APIView):
    def get(self, request):
        pass
    def post(self, request):
        pass
    def put(self, request): #метод для полной замены данных обьекта.
        pass
    def delete(self, request):
        pass
    def patch(self, request): #метод для частичной замены, только некоторых, данных обьекта.
        pass

class BasketView(APIView):
    def get(self, request):
        pass
    def post(self, request):
        pass
    def put(self, request): #метод для полной замены данных обьекта.
        pass
    def delete(self, request):
        pass
    def patch(self, request): #метод для частичной замены, только некоторых, данных обьекта.
        pass


class OrderView(APIView):
    def get(self, request):
        pass
    def post(self, request):
        pass
    def put(self, request): #метод для полной замены данных обьекта.
        pass
    def delete(self, request):
        pass
    def patch(self, request): #метод для частичной замены, только некоторых, данных обьекта.
        pass