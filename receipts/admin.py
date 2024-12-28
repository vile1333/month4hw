from django.contrib import admin
from .models import Recipe,Ingredient,Collection

admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(Collection)

# Register your models here.
