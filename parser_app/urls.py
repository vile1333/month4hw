from django.urls import path
from . import views

urlpatterns = [
    path('litres_book_list/', views.LitresListView.as_view(), name='litres_list'),
        path('form_parser_litres/', views.LitresFormView.as_view()),

]