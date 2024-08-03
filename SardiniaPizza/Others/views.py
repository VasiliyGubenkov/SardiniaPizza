from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    x = {"title": "SardiniaPizza",
         "comment": ["Главная страница сайта", "Вторичная страница сайта"],
         "description": "Это мой пет-проект пиццерии",
         "autorization": True,
         "hello": "Hello, User!"}
    return render(request, 'templates_others/index.html', context=x)

def about(request):
    return HttpResponse("<h1>About</h1>")





