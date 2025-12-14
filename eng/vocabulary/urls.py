from django.urls import path
from . import views

app_name = "vocabulary"

urlpatterns = [
    path("search/", views.search_word, name="search"),
    path("word/<int:word_id>/", views.word_detail_stub, name="word_detail"),
]