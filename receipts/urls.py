from django.urls import path
from .views import CollectionDetailView, RecipeListView  ,RecipeDetailView,RecipeCreateView,IngredientCreateView,RecipeDeleteView,CollectionListView,CollectionCreateView



urlpatterns = [
    path('recipe/', RecipeListView.as_view(), name='recipe_list'),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipe/new/', RecipeCreateView.as_view(), name='recipe_create'),
    path('recipe/<int:recipe_id>/ingredient/new/', IngredientCreateView.as_view(), name='ingredient_create'),
    path('recipe/<int:pk>/delete/', RecipeDeleteView.as_view(), name='recipe_delete'),
    path('collections/', CollectionListView.as_view(), name='collection_list'),
    path('collections/new/', CollectionCreateView.as_view(), name='collection_create'),
    path('collections/<int:pk>/', CollectionDetailView.as_view(), name='collection_detail'),
]