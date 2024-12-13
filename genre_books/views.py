from django.shortcuts import render
from . import models


def all_genre(request):
    if request.method == 'GET':
        genres = models.Genre.objects.all().order_by('-id')
        context = {'genres': genres}
        return render(request, 'tags/all_genres.html', context = context)

def baby_genre(request):
    if request.method == 'GET':
        genres_baby = models.Genre.objects.filter(tags__name = 'Книги для детей').order_by('-id')
        context = {'genres_baby': genres_baby}
        return render(request, 'tags/baby_genres.html', context = context)

def teenager_genre(request):
    if request.method == 'GET':
        genres_teenager = models.Genre.objects.filter(tags__name = 'Книги для подростков').order_by('-id')
        context = {'genres_teenager': genres_teenager}
        return render(request, 'tags/teenager_genres.html', context = context)

def youth_genre(request):
    if request.method == 'GET':
        genres_youth = models.Genre.objects.filter(tags__name = 'Книги для молодежи').order_by('-id')
        context = {'genres_youth': genres_youth}
        return render(request, 'tags/youth_genres.html', context = context)

def pensioner_genre(request):
    if request.method == 'GET':
        genres_pensioner = models.Genre.objects.filter(tags__name = 'Книги для пенсионеров').order_by('-id')
        context = {'genres_pensioner': genres_pensioner}
        return render(request, 'tags/pensioner_genres.html', context = context)





# Create your views here.
