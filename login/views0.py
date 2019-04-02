# 业务逻辑
from django.shortcuts import render,redirect,get_object_or_404
from .models import *  # 导入models文件

from django.http import HttpResponse,HttpResponseRedirect,JsonResponse



# import json



# Create your views here.
def login(request):
    # 通过下面的if语句，我们不允许重复登录：重定向
    if request.session.get('is_login')==True:
        return  redirect('/login/index/')
    if request.method == 'POST':
        # 模板中输入的信息变量
        username=request.POST.get('username')
        password=request.POST.get('password')
        message="所有字段都必须填写"
        # 确保用户名和密码都不为空
        if username and password:
            # 将账号去除空格 并传给 username变量
            username = username.strip()
            try:

                #get(user)为数据库的字段变量  user是一条查询信息
                userinfo = get_object_or_404(UserInfo, user=username)
                # userinfo =UserInfo.objects.get(user=username)

                #如果用户名密码正确 跳转首页
                if userinfo.pwd==password:
                    #设置session变量
                    request.session['is_login'] = True
                    request.session['user_id'] = userinfo.id
                    request.session['user_name'] = userinfo.user

                    return render(request,'login/index.html')

                # 密码错误打印 密码错误提示
                else:
                    message = '密码错误'

            except:
                # 该用户不存在 打印 该用户不存在
                message = '该用户名不存在'

        return render(request, 'login/login.html',locals())

    return render(request,'login/login.html')


def index(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        message = "所有字段都必须填写"
        # 确保用户名和密码都不为空
        if username and password:
            # 将账号去除空格 并传给 username变量

            try:

                # get(user)为数据库的字段变量  user是一条查询信息
                userinfo = get_object_or_404(UserInfo, user=username)
                # userinfo =UserInfo.objects.get(user=username)

                # 如果用户名相等则提示已存在 否则进行存储
                if userinfo.user==username:
                    message ='用户名已存在'
                else:
                    UserInfo.objects.create(user=username, pwd=password)
                    message = '用户提交成功'
            except:
                UserInfo.objects.create(user=username, pwd=password)
                message = '用户提交成功'
        return render(request, 'login/index.html',locals())

    # 从数据库中读取所有数据，注意缩进
    user_list = UserInfo.objects.all()

    return render(request, 'login/index.html', {'data':user_list})


def logout(request):
    # flush次性将session中的所有内容全部清空
    request.session.flush()
    return render(request,'login/login.html')


# return HttpResponse('hello world!')


def json1(request):

    return render(request,'login/json1.html')

def json2(request):

    data= {'a': 'admin', 'b': '123456'}
    return JsonResponse(data)

def table(request):
    return render(request,'login/table.html')

