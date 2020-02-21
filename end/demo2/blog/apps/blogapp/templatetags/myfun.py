from django.template import Library

from ..models import Article,Category,Tag

register = Library()


@register.filter
def date_format(data):
    return "%d-%d-%d"%(data.year,data.month,data.day)


@register.filter
def author_format(author,info):
    return info+":"+author.upper()


@register.simple_tag
def get_latest_articles(num=3):
    return Article.objects.all().order_by('-create_time')[:num]


@register.simple_tag
def get_latest_dates(num=3):
    return Article.objects.dates("create_time", 'month', "DESC")[:num]


@register.simple_tag
def get_category():
    return Category.objects.all().order_by("-id")


@register.simple_tag
def get_tags():
    return Tag.objects.all().order_by("-id")