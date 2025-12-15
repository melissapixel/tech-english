import re
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def highlight_word(text, word):
    if not text or not word:
        return text
    escaped_word = re.escape(word)  # Экранируем спецсимволы в слове (например, "don't" → "don\'t")
    
    pattern = re.compile(rf'\b({escaped_word})\b', re.IGNORECASE)   # \b — граница слова, чтобы не подсвечивать "cat" в "education"

    highlighted = pattern.sub(r'<u class="highlight">\1</u>', text)   # Оборачиваем найденное слово в <u> (или <span>)
    
    return mark_safe(highlighted)