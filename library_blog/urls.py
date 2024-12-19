from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookListView.as_view(), name='books'),
    path('search/', views.BookSearchView.as_view(), name='search'),
    path('book_detail/<int:id>/', views.BookDetailView.as_view(), name='book_detail'),
    path('about_me/', views.AboutMeView.as_view(), name='about_me'),
    path('book_detail/<int:id>/comment/', views.CreateCommentView.as_view(), name='create_comment'),
    path('about_pets/', views.AboutPetsView.as_view(), name='about_pets'),
    path('system_time/', views.SystemTimeView.as_view(), name='system_time'),
]