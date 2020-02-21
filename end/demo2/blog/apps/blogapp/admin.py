from django.contrib import admin
from .models import Ads,Category,Tag,Article,Comment
# Register your models here.
admin.site.register(Ads)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Article)
admin.site.register(Comment)
