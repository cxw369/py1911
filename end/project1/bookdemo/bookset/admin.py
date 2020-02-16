from django.contrib import admin
from django.contrib.admin import ModelAdmin
# Register your models here.

from .models import Book, Hero, User


class HeroInline(admin.StackedInline):
    model = Hero
    # 关联个数
    extra = 1


class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "pub_date")
    list_filter = ("title", "price")
    search_fields = ("title", "price")
    list_per_page = 1
    inlines = [HeroInline]


class HeroAdmin(admin.ModelAdmin):
    list_display = ("name", "gender", "content", "book")
    list_filter = ("name", "gender", "book")
    search_fields = ("name", "gender")
    list_per_page = 1


admin.site.register(Book, BookAdmin)
admin.site.register(Hero, HeroAdmin)
admin.site.register(User)
