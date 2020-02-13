# 引入路由绑定函数
from django.conf.urls import url
from . import views

# 2.每一个路由文件中必须编写路由数组
urlpatterns = [
    url(r"^index/$", views.index),
    url(r"^about/$", views.about),
    # 使用正则分组可以向视图函数中传递参数
    # 正则分组中小括号匹配的内容会作为实参传递给视图函数
    url(r"detail/(\d+)/", views.detail)
]