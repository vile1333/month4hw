from django.db import models


class BookModel(models.Model):
    GENRE = (
        ('Роман','Роман'),
        ('Миф', 'Миф'),
        ('Сказка','Сказка')
    )


    image = models.ImageField(upload_to='book_images/',verbose_name= 'Загрузите фото книги')
    title = models.CharField(max_length=100,verbose_name= 'Укажите название книги')
    description = models.TextField(verbose_name='Укажите описание', blank=True)
    price = models.FloatField(verbose_name='Укажите цену', default= 10)
    created_at = models.DateField(auto_now_add=True)
    genre = models.CharField(max_length=100,choices=GENRE,default='Роман')
    mail = models.EmailField(max_length=100,verbose_name='Укажите почту')
    author = models.CharField(max_length=100,verbose_name='Укажите автора')
    trailer = models.URLField(verbose_name='Укажите ссылку на книгу')

    class Meta:
        verbose_name = 'книгу'
        verbose_name_plural = 'книги'

    def __str__(self):
        return self.title

class Review(models.Model):
    STARS = (
        ('⭐','⭐'),
        ('⭐⭐', '⭐⭐'),
        ('⭐⭐⭐', '⭐⭐⭐'),
        ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
        ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐')
    )


    book = models.ForeignKey(BookModel,on_delete=models.CASCADE,related_name='reviews')
    created_at = models.DateField(auto_now_add=True)
    text_review = models.TextField(verbose_name='Отзыв о книге')
    stars = models.CharField(max_length=100,verbose_name='Поставьте оценку',choices=STARS,default='⭐')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


    def __str__(self):
        return f'{self.book} : {self.stars}'
# Create your models here.
