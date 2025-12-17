from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    slug = models.SlugField('Слаг', unique=True)
    content = models.TextField('Содержание')

    # Новое поле — заглавная картинка
    image = models.ImageField(
        'Превью',
        upload_to='blog/images/',  # будет сохранять файлы в MEDIA_ROOT/blog/images/
        blank=True,                # необязательное
        null=True
    )

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
    
    @property
    def has_image(self):
        # """Удобный способ проверить, есть ли картинка"""
        return self.image and hasattr(self.image, 'url')