from django.contrib import admin

# Register your models here.
from book.models import BookInfo,PeopleInfo

# 注册类模型
admin.site.register(BookInfo)
admin.site.register(PeopleInfo)


