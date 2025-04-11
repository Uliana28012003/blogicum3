from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Category, Post

def index(request):
    # Главная страница: 5 последних публикаций с фильтрами
    post_list = Post.objects.filter(
        is_published=True,                  # Публикация опубликована
        pub_date__lte=timezone.now(),       # Дата публикации не позже текущего времени
        category__is_published=True         # Категория опубликована
    ).order_by('-pub_date')[:5]             # Сортировка по убыванию даты, первые 5
    return render(request, 'blog/index.html', {'post_list': post_list})

def post_detail(request, id):
    # Страница отдельной публикации с фильтрами и ошибкой 404
    post = get_object_or_404(Post.objects.filter(
        is_published=True,                  # Публикация опубликована
        pub_date__lte=timezone.now(),       # Дата публикации не позже текущего времени
        category__is_published=True         # Категория опубликована
    ), id=id)                               # Фильтр по первичному ключу
    return render(request, 'blog/detail.html', {'post': post})

def category_posts(request, category_slug):
    # Страница категории: посты с фильтрами и ошибка 404 для неопубликованной категории
    category = get_object_or_404(Category, slug=category_slug, is_published=True)
    post_list = Post.objects.filter(
        category=category,                  # Принадлежит выбранной категории
        is_published=True,                  # Публикация опубликована
        pub_date__lte=timezone.now()        # Дата публикации не позже текущего времени
    ).order_by('-pub_date')                 # Сортировка по убыванию даты
    return render(request, 'blog/category.html', {
        'category': category,
        'post_list': post_list
    })