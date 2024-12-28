from django.db import models



class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепты"


class Ingredient(models.Model):
    UNIT_CHOICES = [
        ('g', 'граммы'),
        ('kg', 'килограммы'),
        ('ml', 'миллилитры'),
        ('l', 'литры'),
        ('pcs', 'штуки'),
    ]

    name = models.CharField(max_length=100)
    quantity = models.FloatField()
    unit = models.CharField(max_length=10, choices=UNIT_CHOICES)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredients')
    is_optional = models.BooleanField(default=False)
    calories = models.FloatField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ингридиент"
        verbose_name_plural = "Ингриденты"

class Collection(models.Model):
    name = models.CharField(max_length=200)
    recipes = models.ManyToManyField(Recipe, related_name='collections')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Коллекция'
        verbose_name_plural = 'Коллекции'