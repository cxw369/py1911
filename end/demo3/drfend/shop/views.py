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
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

# 通过api_view装饰器可以将基于函数的视图转换为APIVIEW基于类的视图
@api_view(["GET","POST"])
def categoryList(request):
    if request.method == "GET":
        print("获取到GET请求参数",request.query_params)
        queryset = Category.objects.all()
        seria = CategorySerializer(instance=queryset,many=True)
        return Response(seria.data,status=status.HTTP_200_OK)
    elif request.method == "POST":
        print("获取到POST请求参数",request.data)
        # data为序列化对象 来源于请求中提取的数据
        seria = CategorySerializer(data=request.data)
        # 从请求中提取的数据序列化之前要进行检验
        if seria.is_valid():
            seria.save()
            return Response(data=seria.data,status=status.HTTP_201_CREATED)
        else:
            return Response(data=seria.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET","PUT","PATCH","DELETE"])
def categoryDetail(request,cid):
    model = get_object_or_404(Category,pk=cid)
    if request.method == "GET":
        print("获取到GET请求参数", request.query_params)
        seria = CategorySerializer(instance=model)
        return Response(seria.data,status=status.HTTP_200_OK)
    elif request.method == "PUT" or request.method == "PATCH":
        # 更新就是从请求中提取参数 替换数据库中提取的数据
        seria = CategorySerializer(instance=model,data=request.data)
        # 验证是否合法
        if seria.is_valid():
            seria.save()
            return Response(seria.data,status=status.HTTP_200_OK)
        else:
            return Response(seria.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

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
