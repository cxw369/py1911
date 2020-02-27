# from django.db import models
# from django.contrib.auth.models import AbstractUser
# # Create your models here.
#
# class UserManage(models.Manager):
#     """自定义模型管理类 该模型不在具有objects对象"""
#     def deleteUser(self, user_id):
#         # Django默认的objects 是Manage类型
#         user = self.get(user_id)
#         user.delete()
#         user.save()
#
#     def modifyUser(self,user_id):
#         # self.model()可以获取模型类构造函数相当于User()
#         user = self.get(user_id)
#         user.modefy()
#         user.save()
#     def addUser(self,name,limit):
#         user = self.model()
#         user.name = name
#         user.limit = limit
#         user.save()
#
#
# class User(models.Model):
#     name = models.CharField(max_length=8, verbose_name="姓名")
#     account = models.CharField(max_length=10, verbose_name="管理员账号")
#     password = models.CharField(max_length=30,verbose_name="密码")
#     password1 = models.CharField(max_length=30,verbose_name="重复密码")
#     telephone = models.(max_length=20, verbose_name="电话")
#     email = models.EmailField(default="973855683@qq.com", verbose_name="Email")
#     create_time = models.DateField(auto_now_add=True, verbose_name="创建时间")
#
#
# class Role(models.Model):
#     role = models.CharField(max_length=50, verbose_name="角色")
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='roles', verbose_name="所属角色")
#
#
# class Tariff(models.Model):
#     name = models.CharField(max_length=50,verbose_name="资费名称")
#     type = models.CharField(max_length=5,choices=(('1',"包月"),('2','套餐'),('3','计时')),default='2',verbose_name="消费类型")
#     time = models.PositiveIntegerField(verbose_name="基本时长")
#     basic_cost = models.FloatField(verbose_name="基本费用")
#     unit_cost = models.FloatField(verbose_name="单位费用")
#     description = models.FloatField(max_length=100,verbose_name="资费说明")
#     status = models.CharField(max_length=3,choices=(('1','开通'),('2','暂停')),default='1',verbose_name="状态")
#     create_time = models.DateField(auto_now_add=True, verbose_name="创建时间")
#
#
# class Keeper(models.Model):
#     name = models.CharField(max_length=50, verbose_name="姓名")
#     ID_card = models.IntegerField(verbose_name="身份证")
#     login_name = models.CharField(max_length=10, verbose_name="登录名")
#     status = models.CharField(max_length=3, choices=(('1', '开通'), ('2', '暂停'),('3','删除')), default='1', verbose_name="状态")
#     create_time = models.DateField(auto_now_add=True, verbose_name="创建时间")
#     last_time = models.DateField(verbose_name="上次登陆时间")
#
# class Business(models.Model):
#
#
#
#
#
