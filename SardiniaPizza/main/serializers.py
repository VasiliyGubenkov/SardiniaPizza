from rest_framework import serializers
from .models import Pizza, Drink, User, Basket, Order, Category_of_pizza


class CategoryOfPizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category_of_pizza
        fields = '__all__'

class PizzaSerializer(serializers.ModelSerializer):
    category_of_pizza = CategoryOfPizzaSerializer(many=True, read_only=True)
    class Meta:
        model = Pizza
        fields = '__all__'

class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


