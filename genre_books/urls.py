from django.urls import path
from . import views


urlpatterns = [
    path('all_genres/', views.all_genre, name='all_genres'),
    path('baby_genres/', views.baby_genre, name='baby_genres'),
    path('youth_genres/', views.youth_genre, name='youth_genres'),
    path('teenager_genres/', views.teenager_genre, name='teenager_genres'),
    path('pensioner_genres/', views.pensioner_genre, name='pensioner_genres'),
]