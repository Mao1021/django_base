from django.http import HttpResponse,HttpRequest
from django.shortcuts import render

# Create your views here.

#所谓视图就是python函数
# 1.视图函数的第一个参数是接收请求，这个请求其实就是HttpRequest的类对象
# 2.必须返回一个响应
def index(request):

    #第一种
    # return HttpResponse("hello python3")

    #第二种 普遍使用
    # request,template_name,context=None 三个参数
    # request    请求
    # template_name   模板名字
    # context=None,context理解为将视图中的数据传给HTML模板，
    # HTML模板用{{key(变量)}}形式接收context中的key(变量)参数
    context={
        'name':"双12 又惊喜 不容错过"
    }
    return render(request=request,template_name='book/index.html',context=context)
