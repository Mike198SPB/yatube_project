# from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post, Group


# Create your views here.
# def index(request):
#     template = 'posts/index.html'
#     title = 'Это главная страница проекта Yatube'
#     text = 'Последние обновления на сайте'
#     context = {
#         'title': title,
#         'text': text,
#     }
#     return render(request, template, context)

def index(request):
    # Одна строка вместо тысячи слов на SQL:
    # в переменную posts будет сохранена выборка из 10 объектов модели Post,
    # отсортированных по полю pub_date по убыванию (от больших значений к меньшим)
    posts = Post.objects.order_by('-pub_date')[:10]
    # В словаре context отправляем информацию в шаблон
    context = {
        'posts': posts,
        'title': 'Это главная страница проекта Yatube',
        'text': 'Последние обновления на сайте'
    }
    return render(request, 'posts/index.html', context)     


# def group_posts(request, slug):
#     template = 'posts/group_list.html'
#     title = 'Здесь будет информация о группах проекта Yatube'
#     text = 'Лев Толстой – зеркало русской революции'
#     context = {
#         'title': title,
#         'text': text,
#     }
#     return render(request, template, context)

def group_posts(request, slug):
    # Функция get_object_or_404 получает по заданным критериям объект 
    # из базы данных или возвращает сообщение об ошибке, если объект не найден.
    # В нашем случае в переменную group будут переданы объекты модели Group,
    # поле slug у которых соответствует значению slug в запросе
    group = get_object_or_404(Group, slug=slug)

    # Метод .filter позволяет ограничить поиск по критериям.
    # Это аналог добавления
    # условия WHERE group_id = {group_id}
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'group': group,
        'posts': posts,
        'title': group.title,
        'text': group.description
    }
    return render(request, 'posts/group_list.html', context) 