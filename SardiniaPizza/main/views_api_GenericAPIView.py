from rest_framework.generics import GenericAPIView
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *


class PizzaView(mixins.ListModelMixin,
               mixins.CreateModelMixin,
               mixins.UpdateModelMixin,
               mixins.DestroyModelMixin,
               GenericAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer

    def get(self, request, *args, **kwargs):
        query_params = request.query_params
        pizzas = self.queryset

        if query_params:
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

        serializer = self.get_serializer(pizzas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        query_params = request.query_params
        if not query_params:
            return Response({"error": "Нет параметров для поиска нужной пиццы, для последующего обновления"},
                            status=status.HTTP_400_BAD_REQUEST)

        pizza = self.queryset.filter(**query_params).first()
        if pizza:
            serializer = self.get_serializer(pizza, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error": "Пицца с такими параметрами не найдена"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, *args, **kwargs):
        query_params = request.query_params
        if not query_params:
            return Response({"error": "Нет параметров для поиска нужной пиццы, для последующего удаления"},
                            status=status.HTTP_400_BAD_REQUEST)

        pizzas = self.queryset.filter(**query_params)
        if pizzas.exists():
            pizzas.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"error": "Не удалось удалить пиццу с такими параметрами поиска"},
                        status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, *args, **kwargs):
        query_params = request.query_params
        if not query_params:
            return Response({"error": "Нет параметров для поиска нужной пиццы, для последующего обновления"},
                            status=status.HTTP_400_BAD_REQUEST)

        pizza = self.queryset.filter(**query_params).first()
        if pizza:
            serializer = self.get_serializer(pizza, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error": "Пицца с такими параметрами не найдена"}, status=status.HTTP_404_NOT_FOUND)


class DrinkView(mixins.ListModelMixin,
               mixins.CreateModelMixin,
               mixins.UpdateModelMixin,
               mixins.DestroyModelMixin,
               GenericAPIView):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer

    def get(self, request, *args, **kwargs):
        query_params = request.query_params
        drinks = self.queryset

        if query_params:
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

        serializer = self.get_serializer(drinks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        query_params = request.query_params
        if not query_params:
            return Response({"error": "Нет параметров для поиска нужного напитка, для последующего обновления"},
                            status=status.HTTP_400_BAD_REQUEST)

        drink = self.queryset.filter(**query_params).first()
        if drink:
            serializer = self.get_serializer(drink, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error": "Напиток с такими параметрами не найден"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, *args, **kwargs):
        query_params = request.query_params
        if not query_params:
            return Response({"error": "Нет параметров для поиска нужного напитка, для последующего удаления"},
                            status=status.HTTP_400_BAD_REQUEST)

        drinks = self.queryset.filter(**query_params)
        if drinks.exists():
            drinks.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"error": "Не удалось удалить напиток с такими параметрами поиска"},
                        status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, *args, **kwargs):
        query_params = request.query_params
        if not query_params:
            return Response({"error": "Нет параметров для поиска нужного напитка, для последующего обновления"},
                            status=status.HTTP_400_BAD_REQUEST)

        drink = self.queryset.filter(**query_params).first()
        if drink:
            serializer = self.get_serializer(drink, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error": "Напиток с такими параметрами не найден"}, status=status.HTTP_404_NOT_FOUND)


class UserView(mixins.ListModelMixin,
               mixins.CreateModelMixin,
               mixins.UpdateModelMixin,
               mixins.DestroyModelMixin,
               GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BasketView(mixins.ListModelMixin,
                 mixins.CreateModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 GenericAPIView):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer


class OrderView(mixins.ListModelMixin,
                mixins.CreateModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin,
                GenericAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
