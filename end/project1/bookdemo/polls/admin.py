from django.contrib import admin

# Register your models here.
from .models import Title,Alter
from django.contrib.admin import ModelAdmin


class AlteronInline(admin.StackedInline):
    model = Alter
    extra = 5


class AlterAdmin(ModelAdmin):
    list_display = ('choice',)


class TitleAdmin(ModelAdmin):
    list_display = ('name',)
    inlines = [AlteronInline]


admin.site.register(Alter, AlterAdmin)
admin.site.register(Title, TitleAdmin)
