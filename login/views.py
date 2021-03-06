# 业务逻辑
from django.shortcuts import render,redirect,get_object_or_404
from .models import *  # 导入models文件

from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.decorators import login_required
import hashlib
import time


# import json



# Create your views here.
@csrf_exempt
def login(request):
    # 通过下面的if语句，我们不允许重复登录：重定向
    if request.session.get('is_login')==True:
        return  render(request,'login/admin.html')
    if request.method == 'POST':
        # 模板中输入的信息变量
        username=request.POST.get('username')
        password=request.POST.get('password')

        pwd = hashlib.sha1(password.encode("utf8")).hexdigest()  # 对数据进行sha1加密
        print(pwd)
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
                # print(userinfo.pwd)
                if userinfo.pwd==pwd:
                    # print(userinfo.pwd,pwd)
                    #设置session变量
                    request.session['is_login'] = True
                    request.session['user_id'] = userinfo.id
                    request.session['user_name'] = userinfo.user

                    return render(request,'login/admin.html')

                # 密码错误打印 密码错误提示
                else:
                    message = '密码错误'

            except:
                # 该用户不存在 打印 该用户不存在
                message = '该用户名不存在'

        return render(request, 'login/login.html',locals())

    return render(request,'login/login.html')

@csrf_exempt
def submit_login(request):
    # if request.session.get('is_login') != True:
    #     return redirect('/login/')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        message="所有字段都必须填写"

        info = UserInfo()
        #这里要跟数据库字段一致
        info.user = username
        info.pwd = str(password)
        if username and password:
            # 将账号去除空格 并传给 username变量
            try:
                # get(user)为数据库的字段变量  user是一条查询信息
                userinfo = get_object_or_404(UserInfo, user=username)
                # print(userinfo.pwd)
                # userinfo =UserInfo.objects.get(user=username)

                # 如果用户名相等则提示已存在 否则进行存储
                if userinfo.user==username:
                    message = '该用户已存在'
                else:
                    info.save()
                    # UserInfo.objects.create(user=username, pwd=password)
                    message='用户提交成功'
            except:
                # UserInfo.objects.create(user=username, pwd=password)
                info.save()
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




# @csrf_exempt
# def check_submit(request):
#
#     # if request.method == 'POST':
#     username = request.POST.get('username')
#     password = request.POST.get('password')
#     ret = {'code': None, 'msg': None}
#     # if username and password:
#     #         print('ok')
#             # 将账号去除空格 并传给 username变量
#     try:
#         userinfo = get_object_or_404(UserInfo, user=username)
#         print('ok')
#         if userinfo.user==username:
#                 print('ok')
#                 if userinfo.pwd==password:
#
#                     ret['code']=2000
#                     print(ret)
#                     return HttpResponse(json.dumps(ret))
#
#                     # ret['msg']='登录成功'
#
#                 else:
#                     ret['code'] = 2001
#
#                     # ret['msg'] = '密码错误'
#
#         else:
#             ret['code'] = 2009
#             print(ret)
#             # ret['msg'] = '用户名不存在'
#
#     except:
#         pass
#
#
#     return HttpResponse(json.dumps(ret))



    # return HttpResponse(json.dumps(ret))
    # return render(request, 'login/demo.html')

def submit_form(request):
    if request.method == 'POST':
        print(request.POST)
        order_no = str(time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())))+ str(time.time()).replace('.', '')[-7:]
        title=request.POST.get("title")
        money_min=request.POST.get("price_min")
        money_max=request.POST.get('price_max')
        phone=request.POST.get("phone")
        password=request.POST.get("password")
        email=request.POST.get("email")
        city=request.POST.get("city")
        hobbies=request.POST.get("hobbies")
        off_on=request.POST.get("on_off")
        sex=request.POST.get("sex")
        content=request.POST.get("texts")
        search_time=request.POST.get("time1")
        search_times = request.POST.get("times")

        #返回数据
        data = {'status': 200, 'msg': '提交成功', 'data':[money_min,money_max]}
        data1 = {'status': 400, 'msg': '金额错误,最大值必须大于最小值', 'data': [money_min,money_max]}

        #前端的值需转换
        if off_on=='on':
            off_on='True'
        else:
            off_on='False'

        # print(money_min)
        # print(type(money_min))
        if int(float(money_min))<=int(float(money_max)):
            user_form.objects.create(order_no=order_no,title=title,phone=phone,money_min=money_min,
                money_max=money_max,password=password,email=email,city=city,hobbies=hobbies,off_on=off_on,sex=sex
                ,content=content,search_time=search_time,search_times=search_times
            )
            return JsonResponse(data)
        else:
            return JsonResponse(data1)
    else:

        return JsonResponse('请求方法错误')





def user_table(request):

    # 同样支持链式条件过滤查询，如objects.values().filter(book_name=’test’)
    # 支持切片查询，如objects.values()[:10]
    # 支持字段过滤查询，如我只想查询id和book_name
    # 这两个字段，只需这样写
    data=user_form.objects.values().order_by('-id')[:10]
    content={}
    content['list']=list(data)
    content['code']=200
    content['msg']='请求成功'
    # print(len(content['list']))
    return JsonResponse(content)



# @login_required
def demo(request):
    return render(request, 'login/layui_demo.html')


def Active_tab(request):
    return render(request, 'login/Active_tab.html')


@csrf_exempt
def ajax(request):
    if request.method =='POST':
        print(request.POST)
        na=request.POST.get('data')
        # print(na)
        data = {'status': 2001, 'msg': '请求成功', 'data': [11, 22, 33, 4555, 55]}
        data1={'status': 1000, 'msg': '数据错误', 'data':'null'}
        if na=='0000':

            return JsonResponse(data)
        else:
            return JsonResponse(data1)

        # data={'status':0000,'msg':'请求成功','data':[11,22,33,4555,55]}
        # # print(type(JsonResponse(data)))
        # # print(type(json.dumps(data)))
        # return JsonResponse(data)

    else:
        return render(request,'login/ajax.html')







