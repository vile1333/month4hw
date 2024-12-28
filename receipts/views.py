from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .forms import RecipeForm,IngredientForm,CollectionForm
from .models import Recipe, Ingredient , Collection


class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipes/recipe_list.html'
    context_object_name = 'recipes'

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        if query:
            return Recipe.objects.filter(title__icontains=query)
        return Recipe.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        return context

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipes/recipe_detail.html'
    context_object_name = 'recipe'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipe = self.get_object()
        context['total_calories'] = sum(i.calories for i in recipe.ingredients.all() if i.calories)
        return context

class RecipeCreateView(CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipes/recipe_form.html'

    def form_valid(self, form):
        self.object = form.save()
        return redirect('recipe_list')

class IngredientCreateView(CreateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = 'recipes/ingredient_form.html'

    def form_valid(self, form):
        recipe = get_object_or_404(Recipe, pk=self.kwargs['recipe_id'])
        form.instance.recipe = recipe
        self.object = form.save()
        return redirect('recipe_detail', pk=self.kwargs['recipe_id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipe'] = get_object_or_404(Recipe, id=self.kwargs['recipe_id'])
        return context

class RecipeDeleteView(DeleteView):
    model = Recipe
    template_name = 'recipes/recipe_confirm_delete.html'
    success_url = '/recipe'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect('recipe_list')

class CollectionListView(ListView):
    model = Collection
    template_name = 'recipes/collection_list.html'
    context_object_name = 'collections'

class CollectionCreateView(CreateView):
    model = Collection
    form_class = CollectionForm
    template_name = 'recipes/collection_form.html'

    def form_valid(self, form):
        self.object = form.save()
        return redirect('collection_list')

class CollectionDetailView(DetailView):
    model = Collection
    template_name = 'recipes/collection_detail.html'
    context_object_name = 'collection'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipes'] = self.get_object().recipes.all()
        return context
