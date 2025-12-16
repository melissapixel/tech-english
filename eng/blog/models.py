from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    slug = models.SlugField('Слаг', unique=True)
    content = models.TextField('Содержание')
    published = models.BooleanField('Опубликовано', default=False)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):     # стандартный способ получить URL объекта в Django.
        return reverse('blog:post_detail', kwargs={'slug': self.slug})