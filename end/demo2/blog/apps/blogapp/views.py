from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
# 导入分页和分页器
from django.core.paginator import Paginator,Page
from .models import *
from .forms import *
# Create your views here.


def index(request):
    # return HttpResponse("这里是首页")
    ads = Ads.objects.all()
    typepage = request.GET.get("type")
    year = None
    month = None
    category_id = None
    if typepage == "date":
        year = request.GET.get("year")
        month = request.GET.get("month")
        articles = Article.objects.filter(create_time__year=year,create_time__month=month).order_by('-create_time')
    elif typepage == "category":
        category_id = request.GET.get("category_id")
        try:
            category = Category.objects.get(id=category_id)
            articles = category.article_set.all()
        except Exception as e:
            return HttpResponse("分类不合法")
    elif typepage == "tag":
        tag_id = request.GET.get("tag_id")
        try:
            tag = Tag.objects.get(id=tag_id)
            articles = tag.article_set.all()
        except Exception as e:
            return HttpResponse("分类不合法")
    else:
        articles = Article.objects.all().order_by('-create_time')
    # 获取get请求中的页码参数 默认为1
    paginator = Paginator(articles,1)
    num = request.GET.get("pagenum",1)
    page = paginator.get_page(num)
    # locals()可以返回局部变量
    return render(request, 'index.html',locals())


def detail(request,articleid):
    if request.method == "GET":
        # try:
        article = Article.objects.get(id=articleid)
        cf = CommentForm()
        return render(request, 'single.html', locals())
        # except Exception as e:
        #     return HttpResponse("分类不合法")
    elif request.method == "POST":
        cf = CommentForm(request.POST)
        if cf.is_valid():
            # print(cf)
            comment = cf.save(commit=False)
            # 要指明是哪篇文章，不然会报错
            comment.article = Article.objects.get(id=articleid)
            comment.save()
            return redirect(to=reverse("blogapp:detail",args=(articleid,)))
        else:
            article = Article.objects.get(id=articleid)
            cf = CommentForm()
            errors = "输入信息有误"
            return render(request, 'single.html', locals())



def contact(request):
    return render(request, 'contact.html')


def favicon(request):
    # 如果获取logo则重定向到一个图片资源
    return redirect(to="/static/favicon.ico")
