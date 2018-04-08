from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.urls import reverse
# Create your models here.

@python_2_unicode_compatible # 当你想支持python2版本的时候才需要这个装饰器
class Beclass(models.Model):
    def __str__(self):
        return self.class_name
    class_name = models.CharField(max_length=100)


@python_2_unicode_compatible # 当你想支持python2版本的时候才需要这个装饰器
class Hobby(models.Model):
    def __str__(self):
        return self.hobby
    hobby = models.CharField(max_length=100)

@python_2_unicode_compatible # 当你想支持python2版本的时候才需要这个装饰器
class Member(models.Model):
    """docstring for member"""
    class_name = models.ForeignKey(Beclass, on_delete=models.CASCADE) #班级名字
    hobbys = models.ManyToManyField(Hobby)        #爱好
    user_name = models.CharField(primary_key=True,max_length=200)    #成员名字
    sex = models.CharField(max_length=200)          #性别
    birth_time = models.DateTimeField()             #出生日期
    work = models.CharField(max_length=100)         #工作
    description = models.CharField(max_length=400)  #描述信息
    bedroom = models.CharField(max_length=50)       #寝室
    domicile = models.CharField(max_length=400)     #居住地

    def get_absolute_url(self):
        return reverse('ourclass:personalpage', kwargs={'user_name': self.user_name})