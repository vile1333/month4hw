from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='books'),
    path('book_detail/<int:id>/', views.book_detail, name='book_detail'),
    path('about_me/', views.about_me, name='about_me'),
    path('about_pets', views.about_pets, name='about_pets'),
    path('system_time/', views.system_time, name='system_time'),
]