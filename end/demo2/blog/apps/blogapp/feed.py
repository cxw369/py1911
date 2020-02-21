from django.contrib.syndication.views import Feed
from django.shortcuts import reverse
from .models import Article
class ArticcleFeed(Feed):
    title = "动漫吧"
    description = "定期发布一些动漫话题"
    link = "/"

    def items(self):
        return Article.objects.all().order_by("-create_time")[:3]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.body

    def item_link(self, item):
        url = reverse("blogapp:detail",args=(item.id,))
        return url