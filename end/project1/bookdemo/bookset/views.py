from django.shortcuts import render,redirect
from django.template import loader
from django.urls import reverse

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


def delete(request, bookid):
    book = Book.objects.get(id=bookid)
    book.delete()
    return redirect(to="/")


def delete_hero(request, heroid):
    hero = Hero.objects.get(id=heroid)
    bookid = hero.book.id
    hero.delete()
    url = reverse("bookset:detail", args=(bookid,))
    return redirect(to=url)


def add_hero(request, bookid):
    if request.method == "GET":
        return render(request, "addhero.html")
    elif request.method == "POST":
        hero = Hero()
        hero.name = request.POST.get("heroname")
        hero.gender = request.POST.get("sex")
        hero.content = request.POST.get("herocontent")
        hero.book = Book.objects.get(id=bookid)
        hero.save()
        url = reverse("bookset:detail", args=(bookid,))
        return redirect(to=url)


def edithero(request, heroid):
    # 使用get方法进入英雄的编辑页面
    hero = Hero.objects.get(id=heroid)
    if request.method == "GET":
        return render(request, "edithero.html", {'hero': hero})
    elif request.method == "POST":
        hero.name = request.POST.get("heroname")
        hero.gender = request.POST.get("sex")
        hero.content = request.POST.get("herocontent")
        hero.save()
        url = reverse("bookset:detail", args=(hero.book.id,))
        return redirect(to=url)


def add_book(request):
    if request.method == "GET":
        return render(request, "addbook.html")
    elif request.method == "POST":
        book = Book()
        book.title = request.POST.get("booktitile")
        book.price = request.POST.get("bookprice")
        book.pub_date = request.POST.get("bookpub_date")
        book.save()
        return redirect(to="/")


def editbook(request, bookid):
    # 使用get方法进入英雄的编辑页面
    book = Book.objects.get(id=bookid)
    if request.method == "GET":
        return render(request, "editbook.html", {'book': book})
    elif request.method == "POST":
        book.title = request.POST.get("booktitle")
        book.price = request.POST.get("bookprice")
        book.pub_date = request.POST.get("bookpub_date")
        book.save()
        return redirect(to="/")


def about(request):
    return HttpResponse("这里是关于页")