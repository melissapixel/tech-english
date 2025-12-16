from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]

# Теперь ссылки из других приложений:
# <a href="{% url 'blog:post_detail' post.slug %}">Читать</a>