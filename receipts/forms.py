from django.forms import ModelForm
from .models import Recipe, Ingredient, Collection

class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description']

class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name', 'quantity', 'unit', 'is_optional', 'calories', 'notes']

class CollectionForm(ModelForm):
    class Meta:
        model = Collection
        fields = ['name', 'recipes']