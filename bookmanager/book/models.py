from django.db import models

# Create your models here.
class BookInfo(models.Model):
    name=models.CharField(max_length=10)

    #重写 str方法让admin来显示书籍名字
    def __str__(self):
        return self.name

class PeopleInfo(models.Model):
    name=models.CharField(max_length=10)
    gender=models.BooleanField()
    book=models.ForeignKey(BookInfo,on_delete=models.CASCADE)
    def __str__(self):
        return self.name