from django.contrib import admin
from . import models


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'pub_date', 'author')
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    """Класс используется для создания интерфейса комментарий"""

    list_display = ("post", "author", "text", "created")


@admin.register(models.Group)
class GroupAdmin(admin.ModelAdmin):
    """Класс ModelAdmin используется для создания интерфейса в админпанели
    со свойствами:
    Properties
    ----------
    title :
        перечисляем поля, которые должны отображаться в админке"""

    title = ("pk", "title", "slug", "description")
    search_fields = ("pk", "title", "slug", "description",)


@admin.register(models.Follow)
class FollowAdmin(admin.ModelAdmin):
    """Класс используется для создания интерфейса подписок"""

    list_display = ("user", "following")
    empty_value_display = "-пусто-"
