from lib2to3.fixes.fix_input import context

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
import datetime

from django.template.context_processors import request

from . import models,forms
from .forms import ReviewForm
from .models import Review, BookModel
from django.views import generic

class BookSearchView(generic.ListView):
    template_name = 'book.html'
    context_object_name = 'book_list'
    paginate_by = 5

    def get_queryset(self):
        return models.BookModel.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self,*, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context

class BookDetailView(generic.DetailView):
    model = BookModel
    template_name = 'book_detail.html'
    context_object_name = 'book_id'

    def get_object(self,**kwargs):
        book_id = self.kwargs.get('id')
        return get_object_or_404(BookModel, id=book_id)

class BookListView(generic.ListView):
    model = BookModel
    template_name = 'book.html'
    context_object_name = 'book_list'

    def get_queryset(self):
        return BookModel.objects.all().order_by('-id')


class CreateCommentView(generic.CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'comment/create_comment.html'
    context_object_name = 'form'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = get_object_or_404(BookModel, id=self.kwargs['id'])
        context['book'] = book
        return context

    def form_valid(self, form):
        book = get_object_or_404(BookModel, id=self.kwargs['id'])
        review = form.save(commit=False)
        review.book = book
        review.save()
        return redirect('book_detail', id=book.id)

# class CommentListView(generic.ListView):
#     model = Review
#     template_name = 'book_detail.html'
#     context_object_name = 'comment_list'
#     def get_queryset(self):
#         return Review.objects.all().order_by('-id')

class AboutMeView(generic.TemplateView):
    template_name = 'about_me.html'

class AboutPetsView(generic.View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('<img src ="data:image/jpeg;base64,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">')


class SystemTimeView(generic.View):
    def get(self, request, *args, **kwargs):
        x = datetime.datetime.now()
        return HttpResponse(x)


# def book_detail(request, id):
#     if request.method == 'GET':
#         book_id = get_object_or_404(models.BookModel, id=id)
#         context = {
#             'book_id': book_id,
#         }
#         return render(request, 'book_detail.html', context)
#
# #не полная инфа с помощью query запроса
# def book_list(request):
#     if request.method == 'GET':
#         book_list = models.BookModel.objects.all().order_by('-id')
#         context = {
#             'book_list': book_list
#         }
#         return render(request, 'book.html', context)
#
# # def create_comment_view(request):
# #     if request.method == 'POST':
# #         form = ReviewForm(request.POST, request.FILES)
# #         if form.is_valid():
# #             form.save()
# #             return redirect('book_detail', id=form.instance.id)
# #     else:
# #         form = ReviewForm()
# #     return render(request, 'comment/create_comment.html', {'form': form})
#
# def create_comment_view(request, id):
#     book = get_object_or_404(BookModel, id=id)
#     if request.method == 'POST':
#         form = ReviewForm(request.POST, request.FILES)
#         if form.is_valid():
#             review = form.save(commit=False)
#             review.book = book
#             review.save()
#             return redirect('book_detail', id=book.id)
#     else:
#         form = ReviewForm()
#     return render(request, 'comment/create_comment.html', {'form': form, 'book': book})
#
#
# def comment_list_view(request):
#     if request.method == 'GET':
#         comment_list = Review.objects.all().order_by('-id')
#         context = {'comment_list': comment_list}
#         return render(request, 'book_detail.html', context)
#
#
# def about_me(request):
#     if request.method == 'GET':
#         return HttpResponse('Мой первый проект!')
#
# def about_pets(request):
#     if request.method == 'GET':
#         return HttpResponse('<img src ="data:image/jpeg;base64,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 ">')
#
# def system_time(request):
#     if request.method == 'GET':
#         x = datetime.datetime.now()
#         return HttpResponse(x)

# Create your views here.
