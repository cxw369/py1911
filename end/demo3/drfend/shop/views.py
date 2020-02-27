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
