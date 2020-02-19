from django import forms

from .models import User


class LoginForm(forms.Form):
    """
    定义一个登录表单生成html登录表单
    """
    username = forms.CharField(max_length=150,min_length=3,label="请输入用户名",help_text="用户名最少3位数，最大150")
    password = forms.CharField(max_length=150,min_length=3,label="请输入密码",help_text="密码最少3位数，最大150",widget=forms.PasswordInput)


class RegistForm(forms.ModelForm):
    password2 = forms.CharField(widget=forms.PasswordInput,label="重复密码")
    class Meta:
        model = User
        fields = {'username', 'password'}
        labels = {
            'username':'用户名',
            'password':'password'
        }
        help_texts = {
            'username':'最小为3，最大为50',
            'password':'最小为3，最大为50'
        }
        widgets = {
            'password':forms.PasswordInput()
        }


