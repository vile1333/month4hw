from django.shortcuts import render
from genre_books.models import Genre
from django.views import generic


class AllGenreView(generic.ListView):
    model = Genre
    template_name = 'tags/all_genres.html'
    context_object_name = 'genres'

    def get_queryset(self):
        return Genre.objects.all().order_by('-id')


class BabyGenreView(generic.ListView):
    model = Genre
    template_name = 'tags/baby_genres.html'
    context_object_name = 'genres_baby'

    def get_queryset(self):
        return Genre.objects.filter(tags__name='Книги для детей').order_by('-id')


class TeenagerGenreView(generic.ListView):
    model = Genre
    template_name = 'tags/teenager_genres.html'
    context_object_name = 'genres_teenager'

    def get_queryset(self):
        return Genre.objects.filter(tags__name='Книги для подростков').order_by('-id')


class YouthGenreView(generic.ListView):
    model = Genre
    template_name = 'tags/youth_genres.html'
    context_object_name = 'genres_youth'

    def get_queryset(self):
        return Genre.objects.filter(tags__name='Книги для молодежи').order_by('-id')


class PensionerGenreView(generic.ListView):
    model = Genre
    template_name = 'tags/pensioner_genres.html'
    context_object_name = 'genres_pensioner'

    def get_queryset(self):
        return Genre.objects.filter(tags__name='Книги для пенсионеров').order_by('-id')

# def all_genre(request):
#     if request.method == 'GET':
#         genres = models.Genre.objects.all().order_by('-id')
#         context = {'genres': genres}
#         return render(request, 'tags/all_genres.html', context = context)
#
# def baby_genre(request):
#     if request.method == 'GET':
#         genres_baby = models.Genre.objects.filter(tags__name = 'Книги для детей').order_by('-id')
#         context = {'genres_baby': genres_baby}
#         return render(request, 'tags/baby_genres.html', context = context)
#
# def teenager_genre(request):
#     if request.method == 'GET':
#         genres_teenager = models.Genre.objects.filter(tags__name = 'Книги для подростков').order_by('-id')
#         context = {'genres_teenager': genres_teenager}
#         return render(request, 'tags/teenager_genres.html', context = context)
#
# def youth_genre(request):
#     if request.method == 'GET':
#         genres_youth = models.Genre.objects.filter(tags__name = 'Книги для молодежи').order_by('-id')
#         context = {'genres_youth': genres_youth}
#         return render(request, 'tags/youth_genres.html', context = context)
#
# def pensioner_genre(request):
#     if request.method == 'GET':
#         genres_pensioner = models.Genre.objects.filter(tags__name = 'Книги для пенсионеров').order_by('-id')
#         context = {'genres_pensioner': genres_pensioner}
#         return render(request, 'tags/pensioner_genres.html', context = context)





# Create your views here.
