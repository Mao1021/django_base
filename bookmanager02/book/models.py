from django.db import models

# Create your models here.
'''
1.模型类 需要继承model.Model
2.定义属性 
    属性名=model.类型
    2.1属性名=字段名
    不要使用pythn和mysql关键字
    不要使用连续的下划线(__)
    2.2 类型
    类似mysql的类型
    2.3 选项
    CharField必须设置max_length
    verbose_name 主要是站点admin使用
3.改变表的名称
    默认表名为：子应用名_类名 都是小写
'''
class BookInfo(models.Model):

    name=models.CharField(max_length=10,unique=True)
    pub_date=models.DateField(null=True)
    readcount=models.IntegerField(default=0)
    commentcount=models.IntegerField(default=0)
    is_delete=models.BooleanField(default=False)

    class Meta:
        db_table='bookinfo'
        verbose_name='书籍管理'

    def __str__(self):
        return self.name


class PeopleInfo(models.Model):

    # 定义一个有序字典
    GENDER_CHOICE=(
        (1,'male'),
        (2,'female')
    )
    name=models.CharField(max_length=10,unique=True)
    gender=models.SmallIntegerField(choices=GENDER_CHOICE,default=1)
    description=models.CharField(max_length=100,null=True)
    is_delete=models.BooleanField(default=False)

    # 外键
    # 系统会自动添加外键
    # 设置级联操作 on_delete=models.CASCADE
    book=models.ForeignKey(BookInfo,on_delete=models.CASCADE)

    class Meta:
        db_table='peopleinfo'
        verbose_name='人物信息'

    def __str__(self):
        return self.name