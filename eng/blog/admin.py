from django.contrib import admin
from .models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'published', 'created_at']
    list_filter = ['published', 'created_at']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['has_image']     # has_image покажет галочку в списке, если картинка есть.
    
    # Группировка полей
    fieldsets = (
        ('Основное', {
            'fields': ('title', 'slug', 'content', 'image')
        }),
        ('Публикация', {
            'fields': ('published',)
        }),
    )