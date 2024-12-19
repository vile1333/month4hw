from django.urls import path
from . import views


urlpatterns = [
    path('all_genres/', views.AllGenreView.as_view(), name='all_genres'),
    path('baby_genres/', views.BabyGenreView.as_view(), name='baby_genres'),
    path('youth_genres/', views.YouthGenreView.as_view(), name='youth_genres'),
    path('teenager_genres/', views.TeenagerGenreView.as_view(), name='teenager_genres'),
    path('pensioner_genres/', views.PensionerGenreView.as_view(), name='pensioner_genres'),
]