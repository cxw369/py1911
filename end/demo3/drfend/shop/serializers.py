from rest_framework import serializers
from .models import *


# 自定义序列化类
class CustomSerializer(serializers.RelatedField):
    def to_representation(self, value):
        """
        重写字段的输出格式
        :param value: 需要序列化的对象
        :return: 显示的格式
        """
        return str(value.id) + "--" + value.name + "--" + value.desc


class GoodSerializer1(serializers.ModelSerializer):
    # 在序列化时指定字段 在多方使用source=模型名+字段名完成级联关系
    category = serializers.CharField(source='category.name',read_only=True)
    class Meta:
        model = Good
        fields = "__all__"


class CategorySerializer(serializers.Serializer):
    """
    序列化类 决定了序列化的细节
    """
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=10,min_length=3,error_messages={
        "max_length":"最多10个字",
        "min_length":"最少3个字"
    })

    def create(self, validated_data):
        """
        通过重写create方法 来定义模型创建方式
        :param validated_data:
        :return:
        """
        print("重写创建方法",validated_data)
        instance = Category.objects.create(**validated_data)
        print("创建模型实例",instance)
        return instance

    def update(self, instance, validated_data):
        """
        通过重写update 来定义模型的更新方法
        :param instance: 更改之前的实例
        :param validated_data:更改参数
        :return:返回的新实例
        """
        print("重写更新方法",validated_data,instance.name)
        instance.name = validated_data.get("name",instance.name)
        print(instance.name)
        instance.save()
        return instance


class GoodImgsSerializer(serializers.Serializer):
    img = serializers.ImageField()
    good = serializers.CharField(source='good.name')

    def validate(self, attrs):
        print("原始值",attrs["good"]["name"])
        try:
            g = Good.objects.get(name=attrs["good"]["name"])
            print("修改商品",g)
            attrs["good"] = g
        except:
            raise serializers.ValidationError("输入的商品名不存在")
        return attrs

    def create(self, validated_data):
        instance = GoodImgs.objects.create(**validated_data)
        return instance

    def update(self, instance, validated_data):
        """
        通过重写update 来定义模型的更新方法
        :param instance: 更改之前的实例
        :param validated_data:更改参数
        :return:返回的新实例
        """
        print("原始值",instance.img,instance.good)
        instance.img = validated_data.get("img", instance.img)
        instance.good = validated_data.get("good",instance.good)
        print(instance.good)
        instance.save()
        return instance


class GoodSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20, min_length=2, error_messages={
        "max_length": "最多20个字",
        "min_length": "最少2个字"
    })
    category = CategorySerializer(label="分类")
    imgs = GoodImgsSerializer(label="图片",many=True,read_only=True)

    def validate_category(self, category):
        """
        处理category
        :param category: 处理的原始值
        :return: 返回新值
        """
        print("category的原始值为",category)
        try:
            Category.objects.get(name=category["name"])
        except:
            raise serializers.ValidationError("输入的分类名不存在")
        return category


    def validate(self, attrs):
        print("收到的数据为",attrs)
        try:
            c = Category.objects.get(name=attrs["category"]["name"])
        except:
            c = Category.objects.create(name=attrs["category"]["name"])
        attrs["category"] = c
        print("更改之后的数据",attrs)
        return attrs

    def create(self, validated_data):
        print("创建good参数",validated_data)
        instance = Good.objects.create(**validated_data)
        return instance

    def update(self, instance, validated_data):
        """
        通过重写update 来定义模型的更新方法
        :param instance: 更改之前的实例
        :param validated_data:更改参数
        :return:返回的新实例
        """
        print("原始值",instance.name,instance.category)
        instance.name = validated_data.get("name", instance.name)
        instance.category = validated_data.get("category",instance.category)
        print(instance.name)
        instance.save()
        return instance


class CategorySerializer1(serializers.ModelSerializer):
    # goods 一定要和 related_name 的值一样
    # 方法1：StringRelatedField()可以显示关联模型中 __str__的返回值 many=True 代表多个对象
    # goods = serializers.StringRelatedField(many=True)
    # 方法2：
    # goods = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    # 方法3：
    # goods = serializers.HyperlinkedRelatedField(read_only=True,many=True,view_name='good-detail')
    # goods = serializers.SlugRelatedField(slug_field='name',many=True,read_only=True)
    # 自定义序列化类
    # goods = CustomSerializer(many=True,read_only=True)
    goods = GoodSerializer(many=True,read_only=True)

    class Meta:
        model = Category
        fields = "__all__"
