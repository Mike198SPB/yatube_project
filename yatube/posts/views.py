# from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    template = 'posts/index.html'
    title = 'Это главная страница проекта Yatube'
    text = 'Последние обновления на сайте'
    context = {
        'title': title,
        'text': text,
    }
    return render(request, template, context)


def group_posts(request, slug):
    template = 'posts/group_list.html'
    title = 'Здесь будет информация о группах проекта Yatube'
    text = 'Лев Толстой – зеркало русской революции'
    context = {
        'title': title,
        'text': text,
    }
    return render(request, template, context)
