from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Страница приложения esoft")

def categories(request, catid):
    print(request.GET)
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>{catid}</p>')

def archive(request, year):
    return HttpResponse(f'<h1> Архив по годам </h1><p>{year}</p>')