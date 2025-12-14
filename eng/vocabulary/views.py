from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q  # для комбинации услловий в orm 
from .models import Word


# Create your views here.
def search_word(request):
    if request.method == "POST":
        query = request.POST.get("query", "").strip()
        print("🔍 Получен запрос:", repr(query))  # ← Выведет в консоль сервера
        if query:
            word = Word.objects.filter(word_en__iexact=query).first()
            print("🔎 Найдено слово:", word)  # None, если не найдено
            if word:
                print(f"✅ Перенаправляем на слово ID={word.id}")
                return redirect("vocabulary:word_detail", word_id=word.id)
            else:
                return render(request, "vocabulary/search.html", {
                    "error": f'Слово "{query}" не найдено.',
                    "query": query
                })
        else:
            return render(request, "vocabulary/search.html", {"error": "Введите слово."})
    
    return render(request, "vocabulary/search.html")


def word_detail_stub(request, word_id):
    # Позже здесь будет настоящая логика
    word = get_object_or_404(Word, id=word_id)
    return render(request, "vocabulary/word_detail_stub.html", {"word": word})