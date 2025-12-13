from django.db import models

# Create your models here.
class Word(models.Model):
    word_en = models.CharField(
        max_length=100,
        verbose_name="Английское слово"
    )
    translation_ru = models.CharField(
        max_length=200,
        verbose_name="Перевод на русский"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата добавления"
    )

    def __str__(self):
        return f"{self.word_en} → {self.translation_ru}"

    class Meta:
        verbose_name = "Слово"
        verbose_name_plural = "Слова"
        ordering = ['-created_at']


class Phrase(models.Model):
    word = models.ForeignKey(
        Word,
        on_delete=models.CASCADE,
        related_name='phrases',
        verbose_name="Связанное слово"
    )
    example_en = models.TextField(
        verbose_name="Пример на английском"
    )
    translation_ru = models.TextField(
        verbose_name="Перевод"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата добавления"
    )

    def __str__(self):
        return self.example_en[:60] + ("..." if len(self.example_en) > 60 else "")

    class Meta:
        verbose_name = "Фраза"
        verbose_name_plural = "Фразы"
        ordering = ['-created_at']


# Название не Text - чтобы избежать конфликтов с SQL-ключевым словом и типом данных.
class TextExample(models.Model):
    word = models.ForeignKey(
        Word,
        on_delete=models.CASCADE,
        related_name='texts',
        verbose_name="Связанное слово"
    )
    example_en = models.TextField(
        verbose_name="Текст на английском"
    )
    translation_ru = models.TextField(
        verbose_name="Перевод"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата добавления"
    )

    def __str__(self):
        return self.example_en[:60] + ("..." if len(self.example_en) > 60 else "")

    class Meta:
        verbose_name = "Текст (пример)"
        verbose_name_plural = "Тексты (примеры)"
        ordering = ['-created_at']