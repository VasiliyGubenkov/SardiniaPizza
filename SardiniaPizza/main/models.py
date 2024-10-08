from decimal import Decimal
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Category_of_pizza(models.Model):
    name = models.CharField(max_length=100, verbose_name="Категория пиццы", help_text="Создайте категорию пиццы", unique=True, blank=False, null=False,)
    description = models.TextField(verbose_name="Описание категории", help_text="Опишите эту категорию пиццы", blank=True, null=True)
    slug = models.SlugField(max_length=200, verbose_name="URL", help_text="Укажите URL-слаг", unique=True, blank=True, null=True,)
    class Meta():
        db_table = 'Категории пиццы'
        verbose_name='Категорию пиццы'
        verbose_name_plural='Категории пиццы'
    def __str__(self):
        return f"{self.name}, {self.description}"



class Category_of_drinks(models.Model):
    name = models.CharField(max_length=100, verbose_name="Категория напитков", help_text="Создайте категорию напитков", unique=True, blank=False, null=False,)
    description = models.TextField(verbose_name="Описание категории", help_text="Опишите эту категорию напитков", blank=True, null=True)
    slug = models.SlugField(max_length=200, verbose_name="URL", help_text="Укажите URL-слаг", unique=True, blank=True, null=True, )
    class Meta():
        db_table = 'Категории напитков'
        verbose_name = 'Категорию напитков'
        verbose_name_plural = 'Категории напитков'
    def __str__(self):
        return f"{self.name, self.description}"



class Pizza(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название пиццы", help_text="Напишите название пиццы", unique=True, blank=False, null=False,)
    image = models.ImageField(upload_to="pizza/%Y/%m/%d/", verbose_name="Изображение пиццы", help_text="Загрузите сюда ссылку на изображение с пиццей", blank=True, null=True,)
    description = models.TextField(verbose_name="Описание", help_text="Опишите пиццу", null=True, blank=True)
    sizes_of_pizza = [('33cm.', '33cm.'), ('40cm.', '40cm.')]
    size = models.CharField(max_length=100, choices=sizes_of_pizza, verbose_name="Размер пиццы", help_text="Выберите размер пиццы", blank=False, null=False,)
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Цена пиццы", help_text="Укажите цену пиццы", null=False, blank=False,)
    discount = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Скидка на пиццу", help_text="Укажите скидку на пиццу", null=True, blank=True,)
    category_of_pizza = models.ManyToManyField(Category_of_pizza, verbose_name="Категория пиццы", help_text="Выберите категорию пиццы", related_name="pizzas")
    slug = models.SlugField(max_length=200, verbose_name="URL", help_text="Укажите URL-слаг", unique=True, blank=True, null=True, )
    baskets = GenericRelation('Basket')
    class Meta():
        db_table = 'Пиццы'
        ordering = ['name']
        verbose_name='Пиццу'
        verbose_name_plural = 'Пиццы'
    def __str__(self):
        return f"{self.name}"
    def id_on_page(self):
        return f'{self.id : 05}'
    def sell_price(self):
        if self.discount:
            return self.price - (self.price*self.discount/Decimal('100'))
        else:
            return self.price


class Drink(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название напитка", help_text="Напишите название напитка", unique=True, blank=False, null=False,)
    image = models.ImageField(upload_to="pizza/%Y/%m/%d/", verbose_name="Изображение напитка", help_text="Загрузите сюда ссылку на изображение с напитком", blank=True, null=True, )
    description = models.TextField(verbose_name="Описание", help_text="Опишите напиток", null=True, blank=True)
    size = models.CharField(max_length=100, verbose_name="Обьём напитка", help_text="Укажите обьём напитка", blank=False, null=False,)
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Цена напитка", help_text="Укажите цену напитка", null=False, blank=False,)
    discount = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Скидка на напиток", help_text="Укажите скидку на напиток", null=True, blank=True, )
    category_of_drinks = models.ManyToManyField(Category_of_drinks, verbose_name="Категория напитка", help_text="Выберите категорию напитка", related_name="drinks")
    slug = models.SlugField(max_length=200, verbose_name="URL", help_text="Укажите URL-слаг", unique=True, blank=True, null=True, )
    baskets = GenericRelation('Basket')
    class Meta():
        db_table = 'Напитки'
        ordering = ['name']
        verbose_name='Напиток'
        verbose_name_plural = 'Напитки'
    def __str__(self):
        return f"{self.name}"



class User(models.Model):
    user_login = models.CharField(max_length=100, null=True, blank=True, unique=True)
    name = models.CharField(max_length=100, null=False, blank=False,)
    surname = models.CharField(max_length=100, null=False, blank=False,)
    email = models.EmailField(unique=False, null=False, blank=False,)
    phone = models.CharField(max_length=100, null=False, blank=False,)
    slug = models.SlugField(max_length=200, verbose_name="URL", help_text="Укажите URL-слаг", unique=True, blank=True, null=True, )
    class Meta():
        db_table = 'Пользователи'
        verbose_name='Пользователя'
        verbose_name_plural = 'Пользователи'
    def __str__(self):
        return f"{self.name}"


class Basket(models.Model):
    user = models.ForeignKey(User, verbose_name="Пользователь", help_text="Выберите пользователя", on_delete=models.SET_NULL, null=True, blank=True, related_name="basket")
    content_type = models.ForeignKey(ContentType,on_delete=models.CASCADE, limit_choices_to=models.Q(app_label='app_name', model='pizza') | models.Q(app_label='app_name', model='drink'), verbose_name="Тип товара")
    object_id = models.PositiveIntegerField(verbose_name="ID товара")
    good = GenericForeignKey('content_type', 'object_id')
    price_of_good = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Цена товара", help_text="Укажите цену товара", null=False, blank=False, )
    quantity_of_good = models.DecimalField(max_digits=5, decimal_places=0, verbose_name="Количество товара", help_text="Укажите количество товара", null=False, blank=False,  default=1, )
    slug = models.SlugField(max_length=200, verbose_name="URL", help_text="Укажите URL-слаг", unique=True, blank=True, null=True, )
    def save(self, *args, **kwargs):
        if self.good:
            self.price_of_good = self.good.prise
        super().save(*args, **kwargs)
    class Meta():
        db_table = 'Корзины пользователей'
        ordering = ['user']
        verbose_name='Корзину'
        verbose_name_plural = 'Корзины'
    def __str__(self):
        return f"{self.good.name} - {self.quantity_of_good} x {self.price_of_good}"


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name="Пользователь", help_text="Выберите пользователя", related_name="orders", null=True, blank=True,)
    address_of_delivery = models.TextField(verbose_name="Адрес доставки", help_text="Укажите адрес доставки заказа", null=True, blank=True)
    content_of_order = models.TextField(verbose_name="Содержание заказа", help_text="Укажите товары и их количество", null=True, blank=True)
    amount = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Общая сумма заказа", help_text="Укажите общую сумму заказа", null=True, blank=True)
    payment_statuses = [("False", "Не оплачен"), ("True", "Оплачен")]
    status_of_payment = models.BooleanField(default=False, verbose_name="Статус оплаты", help_text="Выберите статус оплаты", choices=payment_statuses, null=True, blank=True)
    delivery_statuses = [("False", "Не доставлено"), ("True", "Доставлено")]
    status_of_delivery = models.BooleanField(default=False, verbose_name="Статус доставки", help_text="Выберите статус доставки", choices=delivery_statuses, null=True, blank=True)
    slug = models.SlugField(max_length=200, verbose_name="URL", help_text="Укажите URL-слаг", unique=True, blank=True, null=True, )
    class Meta():
        db_table = 'Заказы'
        ordering = ['user']
        verbose_name='Заказ'
        verbose_name_plural = 'Заказы'
    def __str__(self):
        return f"Order #{self.id} by {self.user} for the amount {self.amount} paid = {self.status_of_payment}"