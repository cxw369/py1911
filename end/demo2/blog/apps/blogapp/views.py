from django.shortcuts import render,redirect
from django.http import HttpResponse
# 导入分页和分页器
from django.core.paginator import Paginator,Page
from .models import *
# Create your views here.


def index(request):
    # return HttpResponse("这里是首页")
    ads = Ads.objects.all()
    articles = Article.objects.all()
    # 获取get请求中的页码参数 默认为1
    paginator = Paginator(articles,1)
    num = request.GET.get("pagenum",1)
    page = paginator.get_page(num)
    # locals()可以返回局部变量
    return render(request, 'index.html',{"ads":ads,"page":page})


def detail(request,articleid):
    return render(request, 'single.html')


def contact(request):
    return render(request, 'contact.html')


def favicon(request):
    # 如果获取logo则重定向到一个图片资源
    return redirect(to="/static/favicon.ico")
