from django.shortcuts import render
from django.template import loader
from .models import Book,Hero

# Create your views here.
from django.http import HttpResponse


# 3.编写对应的视图函数
def index(request):
    # return HttpResponse("这里是首页")
    # 1.获取模板
    # template = loader.get_template("index.html")
    # 加载模板数据
    books = Book.objects.all()
    # 构造上下文
    # context = {"books": books}
    # 渲染模板
    # result = template.render(context)
    # 将渲染结果使用httpresponse返回
    # return HttpResponse(result)
    # 简写:
    return render(request, "index.html", {"books": books})


def detail(request, bookid):
    # template = loader.get_template("detail.html")
    book = Book.objects.get(id=bookid)
    # context = {"book": book}
    # result = template.render(context)
    # return HttpResponse(result)
    return render(request, 'detail.html', {"book": book})


def about(request):
    return HttpResponse("这里是关于页")