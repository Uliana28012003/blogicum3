from django.contrib import admin
from .models import Category, Location, Post

# Настройка модели Category
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)  # Отображаемые поля в списке
    search_fields = ('title',)  # Поля для поиска

# Настройка модели Location
@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)

# Настройка модели Post
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'is_published', 'author', 'category', 'location')
    list_filter = ('is_published', 'category', 'location')  # Фильтры
    search_fields = ('title', 'text')  # Поиск по заголовку и тексту
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'description', 'text', 'pub_date', 'is_published', 
                       'author', 'category', 'location')
        }),
    )

    # Подсказки к полям
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['is_published'].help_text = 'Снимите галочку, чтобы скрыть публикацию.'
        form.base_fields['slug'].help_text = (
            'Идентификатор страницы для URL; разрешены символы латиницы, цифры, дефис и подчёркивание.'
        )
        form.base_fields['pub_date'].help_text = (
            'Если установить дату и время в будущем — можно делать отложенные публикации.'
        )
        return form