from django.db import models
from django.db.models import ForeignKey

from library_blog.models import BookModel


class Basket(models.Model):
    name = models.CharField(max_length=100,verbose_name='Имя')
    mail = models.EmailField(max_length=100,verbose_name='Почта')
    phone_number = models.CharField(max_length=100, verbose_name='Телефон')
    book = ForeignKey(BookModel, on_delete=models.CASCADE,related_name='buy_book',null=True,verbose_name='Книга')

    def __str__(self):
        return self.name


# Create your models here.
