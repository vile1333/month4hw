from django.db import models

class LitresModel(models.Model):
    title = models.CharField(max_length=100)
    image = models.URLField(max_length=200)
    formats = models.CharField(max_length=100)
    price = models.CharField(max_length=100)

    def __str__(self):
        return self.title

# Create your models here.
