from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


    class Meta:
        ordering = ['-published_at', '-title']

    def __str__(self):
        return self.title


# My code
class Category(models.Model):
    name = models.CharField(max_length=65, verbose_name='Категория')
    articles = models.ManyToManyField(Article, through='Compilation')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Compilation(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_main = models.BooleanField(default=False, verbose_name='Основной')

    class Meta:
        verbose_name = 'Связь'
        verbose_name_plural = 'Связи'
        ordering = ['-is_main', 'category']

    def __str__(self):
        return f'{self.category}'


