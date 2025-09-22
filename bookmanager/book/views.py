from django.http import HttpResponse,HttpRequest
from django.shortcuts import render

# Create your views here.

#所谓视图就是python函数
# 1.视图函数的第一个参数是接收请求，这个请求其实就是HttpRequest的类对象
# 2.必须返回一个响应
def index(request):

    return HttpResponse("hello python3")

