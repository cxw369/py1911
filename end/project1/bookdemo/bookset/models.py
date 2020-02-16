from django.db import models

# Create your models here.


class Book(models.Model):
    """
    book继承了Model类。因为Model类拥有操作数据库的功能
    """
    title = models.CharField(max_length=20)
    pub_date = models.DateField(default="1983-06-01")
    price = models.FloatField(default=25)
    author = models.CharField(max_length=20,default="cxw")
    desc = models.CharField(max_length=50,null=True,blank=True,db_column="description")

    def __str__(self):
        return self.title


class Hero(models.Model):
    """
    hero继承了Model,也可以操作数据库
    """
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=6, choices=(('male', '男'), ('female', '女')), default='male')
    content = models.CharField(max_length=100)
    # book 是一对多中的外键 on_delete代表删除主表数据时如何做
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="heros")

    def __str__(self):
        return f"{self.name}=={self.gender}"


class UserManage(models.Manager):
    """自定义模型管理类 该模型不在具有objects对象"""
    def deleteByTelePhone(self, tele):
        # Django默认的objects 是Manage类型
        user = self.get(telephone=tele)
        user.delete()
        user.save()

    def createUser(self,tele):
        # self.model()可以获取模型类构造函数相当于User()
        user = self.model()
        user.telephone = tele
        user.save()


class User(models.Model):
    telephone = models.CharField(max_length=11, null=True, blank=True, verbose_name="手机号码")
    # 自定义过管理字段之后不再有objects 自定义了一个新的objects
    objects = UserManage()

    def __str__(self):
        return self.telephone

    class Meta:
        # 表明
        db_table = "用户类"
        ordering = ["-telephone"]
        # ordering页面进入模型类显示名字
        verbose_name = "用户模型类a"
        # admin 页面在应用下方显示的模型名
        verbose_name_plural = "用户模型类s"


class Acount(models.Model):
    username = models.CharField(max_length=20,verbose_name="用户名")
    password = models.CharField(max_length=20, verbose_name="密码")
    regist_date = models.DateField(auto_now_add=True, verbose_name="注册日期")


class Concact(models.Model):
    telephone = models.CharField(max_length=11,verbose_name="手机号")
    email = models.EmailField(default="973855683@qq.com")
    account = models.OneToOneField(Acount, on_delete=models.CASCADE, related_name="con")


class Article(models.Model):
    title = models.CharField(max_length=20, verbose_name="标题")
    summary = models.TextField(verbose_name="正文")


class Tag(models.Model):
    name = models.CharField(max_length=10, verbose_name="标签名")
    articles = models.ManyToManyField(Article, related_name="tags")