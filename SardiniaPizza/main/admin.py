from django.contrib import admin
from .models import *

# admin.site.register(Category_of_pizza)
# admin.site.register(Category_of_drinks)
# admin.site.register(Pizza)
# admin.site.register(Drink)
# admin.site.register(User)
# admin.site.register(Basket)
# admin.site.register(Order)


@admin.register(Category_of_pizza)
class Category_of_pizza_Admin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    list_filter = ('name',)
    ordering = ('name',)
    list_per_page = 20


@admin.register(Category_of_drinks)
class Category_of_drinks_Admin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    list_filter = ('name',)
    ordering = ('name',)
    list_per_page = 20


@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'size', 'price', 'discount')
    search_fields = ('name',)
    list_filter = ('name',)
    ordering = ('price',)
    list_per_page = 20


@admin.register(Drink)
class DrinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'size', 'price', 'discount')
    search_fields = ('name',)
    list_filter = ('name',)
    ordering = ('price',)
    list_per_page = 20


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_login', 'name', 'surname', 'phone', 'email')
    search_fields = ('user_login', 'name', 'surname', 'phone', 'email')
    list_filter = ('user_login', 'name', 'surname', 'phone', 'email')
    ordering = ('name',)
    list_per_page = 20


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ('user', 'good', 'price_of_good', 'quantity_of_good')
    search_fields = ('user', 'good', 'price_of_good', 'quantity_of_good')
    list_filter = ('user', 'good', 'price_of_good', 'quantity_of_good')
    ordering = ('user',)
    list_per_page = 20


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'address_of_delivery', 'content_of_order', 'amount', 'payment_statuses')
    search_fields = ('user', 'address_of_delivery', 'content_of_order', 'amount', 'payment_statuses')
    list_filter = ('user', 'address_of_delivery', 'content_of_order', 'amount', 'status_of_payment')
    ordering = ('user',)
    list_per_page = 20



