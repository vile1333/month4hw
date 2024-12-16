from django.urls import path
from . import views

urlpatterns = [
    path('basket_list/', views.basket_list_view, name='basket_view'),
    path('basket_list/<int:id>/', views.basket_detail_view, name='basket_detail_view'),
    path('basket_list/<int:id>/update/', views.basket_update_view, name='basket_update_view'),
    path('basket_list/<int:id>/delete/', views.basket_delete_view, name='basket_delete_view'),
    path('create_basket/', views.create_basket_view, name='create_basket'),
]