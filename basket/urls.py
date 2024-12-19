from django.urls import path
from . import views

urlpatterns = [
    path('basket_list/', views.BasketListView.as_view(), name='basket_view'),
    path('basket_list/<int:id>/', views.BasketDetailView.as_view(), name='basket_detail_view'),
    path('basket_list/<int:id>/update/', views.UpdateBasketView.as_view(), name='basket_update_view'),
    path('basket_list/<int:id>/delete/', views.DeleteBasketView.as_view(), name='basket_delete_view'),
    path('create_basket/', views.CreateBasketView.as_view(), name='create_basket'),
]