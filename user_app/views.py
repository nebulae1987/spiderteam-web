from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from user_app.models import User

def index(request):
    '''主页'''
    return render(request,'index.html')
def loginPage(request):
    '''
    登录页面
    :return:
    '''
    return render(request,'login.html')

def loginLogic(request):
    '''
    登录逻辑 处理
    :return:
    '''
    username = request.POST.get('userid')
    password = request.POST.get('psw')
    print(username,password)
    try:
        user = User.objects.filter(username=username,password=password)
        if user:
            request.session['login'] = 1    # 登录成功后创建登录状态session
            return HttpResponse('1')
        else:
            return HttpResponse('0')
    except:
        return HttpResponse('登录异常！')

def registPage(request):
    '''
    注册页面
    :return:
    '''
    return render(request,'register.html')

def registLogic(request):
    '''
    注册逻辑
    :return:
    '''
    print('registLogic ')
    username = request.POST.get('userid')
    usertel = request.POST.get('usrtel')
    email = request.POST.get('email')
    question = request.POST.get('question')
    answer = request.POST.get('answer')
    psw = request.POST.get('psw')
    question_answer = question+':'+answer
    print('post:',username,usertel,email,question,answer,psw)
    try:
        User.objects.create(username=username,phone=usertel,password=psw,email=email,remark=question_answer)
        return HttpResponse('success')
    except:
        print('注册失败！')
        return HttpResponse('faild')

def checkEmail(request):
    '''
    注册时，异步检测邮箱是否已被注册
    :param request:
    :return:
    '''
    user_email = request.GET.get('user_email')
    try:
        emailDatas = User.objects.filter(email=user_email)

        if not emailDatas:
            return HttpResponse('1')
        else:
            return HttpResponse('0')
    except:
        return HttpResponse('邮箱异常！')

def forgetPwdPage(request):
    '''
    忘记密码页面
    :param request:
    :return:
    '''
    return render(request,'forget_pwd.html')
def forgetLogic(request):
    '''
    忘记密码验证
    :param request:
    :return:
    '''
    email = request.POST.get('email')
    question = request.POST.get('question')
    answer = request.POST.get('answer')
    try:
        checkUser = User.objects.filter(email=email)
        if checkUser and checkUser[0].remark == question+':'+answer:
            request.session['checkEmail'] = email
            return HttpResponse('1')
        else:
            return HttpResponse('0')
    except:
        return HttpResponse('验证异常！请重试')

def changePwdPage(request):
    '''
    修改用户密码页面
    :param request:
    :return:
    '''
    checkEmail = request.session.get('checkEmail')
    return render(request,'change_pwd.html',{'checkEmail':checkEmail})

def changePwd(request):
    '''
    修改新密码
    :param request:
    :return:
    '''
    email = request.POST.get('checkEmail')
    newPwd = request.POST.get('password')
    try:
        user = User.objects.filter(email=email)[0]
        if user:
            user.password = newPwd
            user.save()
            return HttpResponse('1')
        else:
            return HttpResponse('0')
    except:
        return HttpResponse('修改异常！请重试')