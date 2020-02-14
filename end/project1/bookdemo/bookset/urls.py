# 引入路由绑定函数
from django.conf.urls import url
from . import views


app_name = "bookset"

# 2.每一个路由文件中必须编写路由数组
urlpatterns = [
    url(r"^$", views.index, name="index"),
    url(r"^about/$", views.about, name="about"),
    # 使用正则分组可以向视图函数中传递参数
    # 正则分组中小括号匹配的内容会作为实参传递给视图函数
    url(r"detail/(\d+)/$", views.detail, name="detail"),
    url(r"delete/(\d+)/$", views.delete, name="delete"),
    url(r"delete_hero/(\d+)/$", views.delete_hero, name="delete_hero"),
    url(r"add_hero/(\d+)/$", views.add_hero, name="add_hero"),
    url(r"edithero/(\d+)/$", views.edithero, name="edithero"),
    url(r"add_book/$", views.add_book, name="add_book"),
    url(r"editbook/(\d+)/$", views.editbook, name="editbook"),
]