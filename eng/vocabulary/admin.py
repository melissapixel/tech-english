from django.contrib import admin
from .models import Word, Phrase, TextExample

# Register your models here.
@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ['word_en', 'translation_ru', 'created_at']
    search_fields = ['word_en', 'translation_ru']

@admin.register(Phrase)
class PhraseAdmin(admin.ModelAdmin):
    list_display = ['word', 'example_en', 'created_at']
    list_filter = ['created_at']
    search_fields = ['example_en', 'translation_ru']

@admin.register(TextExample)
class TextExampleAdmin(admin.ModelAdmin):
    list_display = ['word', 'example_en', 'created_at']
    list_filter = ['created_at']
    search_fields = ['example_en', 'translation_ru']