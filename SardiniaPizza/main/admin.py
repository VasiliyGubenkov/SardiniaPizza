from django.contrib import admin
from .models import *

admin.site.register(Category_of_pizza)
admin.site.register(Category_of_drinks)
admin.site.register(Pizza)
admin.site.register(Drink)
admin.site.register(User)
admin.site.register(Basket)
admin.site.register(Order)
#
# @admin.register(Category_of_pizza)
# class CategoryAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'slug': ('category_pizza_name',)}
#
# @admin.register(Category_of_drinks)
# class CategoryAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'slug': ('category_drinks_name',)}
#
# @admin.register(Pizza)
# class PizzaAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'slug': ('pizza_name',)}
#
# @admin.register(Drink)
# class DrinkAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'slug': ('drink_name',)}
#
# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'slug': ('user_name',)}
#
# @admin.register(Basket)
# class BasketAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'slug': ('basket_name',)}
#
# @admin.register(Order)
# class OrderAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'slug': ('order_name',)}


