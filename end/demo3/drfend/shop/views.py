# from django.shortcuts import render
# from django.http import HttpResponse,JsonResponse
# from .models import *
# from django.core import serializers
# Create your views here.

# 前后端分离
# def index(request):
#     # 如果以json或者xml返回数据，则可以实现前后端分离
#     categorys = Category.objects.all()
#     # 使用Django自带的序列化模块完成序列化
#     result = serializers.serialize("json",categorys)
#     return JsonResponse(result,safe=False)
#     # 如果使用Django模板就是前后端不分离
#     # return HttpResponse('首页')


# 前后端分离
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from django.http import HttpResponse
from rest_framework.request import Request

# 通过api_view装饰器可以将基于函数的视图转换为APIVIEW基于类的视图
@api_view(["GET","POST"])
def categoryList(request):
    print(request,type(request))
    if request.method == "GET":
        print("获取到GET请求参数",request.query_params)
        return HttpResponse("获取列表成功")
    elif request.method == "POST":
        print("获取到POST请求参数",request.data)
        return HttpResponse("创建成功")


@api_view(["GET","PUT","PATCH","DELETE"])
def categoryDetail(request,cid):
    if request.method == "GET":
        print("获取到GET请求参数", request.query_params)
        return HttpResponse("获取单个成功")
    elif request.method == "PUT" or request.method == "PATCH":
        print("获取到PUT/PATCH请求参数",request.data)
        return HttpResponse("修改成功")
    elif request.method == "DELETE":
        return HttpResponse("删除成功")
    else:
        return HttpResponse("当前路由不允许"+request.method+"操作")


class CategoryViewSets(viewsets.ModelViewSet):
    # 要查询的集合
    queryset = Category.objects.all()
    # 要序列化的类
    # serializer_class = CategorySerializer
    def get_serializer_class(self):
        return CategorySerializer


class GoodViewSets(viewsets.ModelViewSet):
    queryset = Good.objects.all()
    serializer_class = GoodSerializer


class GoodImgsViewSets(viewsets.ModelViewSet):
    queryset = GoodImgs.objects.all()
    serializer_class = GoodImgsSerializer
