"""drfend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from shop.views import *
from .settings import MEDIA_ROOT
from django.conf.urls import url
from django.views.static import serve
# 引入api文档路由
from rest_framework.documentation import include_docs_urls
router = routers.DefaultRouter()
# 可以通过router默认路由注册资源
router.register("categorys",CategoryViewSets2)
router.register("goods",GoodViewSets)
router.register("goodimgs",GoodImgsViewSets)
urlpatterns = [
    path('admin/', admin.site.urls),
    url('media/(?P<path>.*)',serve,{'document_root':MEDIA_ROOT}),
    # 配置RestFulAPI
    path('api/v1/', include(router.urls)),
    # 基于函数
    # url(r'^categorylist/$',categoryList,name="caregorylist"),
    # url(r'^categorydetail/(\d+)/$',categoryDetail,name="categorydetail"),
    # 基于类
    # url(r'^categorylist/$',CategoryListView.as_view(),name="caregorylist"),
    # url(r'^categorydetail/(\d+)/$',CategoryDetailView.as_view(),name="categorydetail"),
    # 基于高级类
    # url(r'^categorylist/$',CategoryListView.as_view(),name="caregorylist"),
    # url(r'^categorydetail/(?P<pk>\d+)/$',CategoryDetailView.as_view(),name="categorydetail"),
    # 终极方法
    # url(r'^categorys/$',CategoryViewSets2.as_view({'get':'list',"post":"create"})),
    # url(r'^categorys/(?P<pk>\d+)/$',CategoryViewSets2.as_view({'get':'retrieve','put':'update','patch':'update','delete':'destroy'})),
    # api文档地址
    path('api/v1/docs', include_docs_urls(title="api",description="v1")),
    # 为了在Drf路由调试界面中能够实现相关功能引入下方路由
    path('', include('rest_framework.urls')),
]
