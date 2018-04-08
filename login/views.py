#encoding:utf-8
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from .models import User
from .forms import UserForm,RegisterForm
# Create your views here.

def index(request):
    pass
    return render(request, 'login/index.html')

#def login(request):
#   if request.method == "POST":
#        username = request.POST.get('username', None)
#        password = request.POST.get('password', None)
#        if username and password:
#            print(username,password)
#            username = username.strip()
#            try:
#                user=User.objects.get(name=username)
#                #return HttpResponse("不存在的用户名，请确认后重新登陆")
#                if user.password == password:
#                    return redirect('/login/index/')
#                else:
#                    message = "密码不正确!"
#                #return HttpResponse("密码错误")
#            except:
#                    message = "用户名不存在！"
#        return render(request, 'login/login.html', {"message": message})
#    return render(request, 'login/login.html')

def login(request):
    if request.session.get('is_login',None):
        return redirect("login/index/")
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            username =  form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                user = User.objects.get(name=username)
                if user.password == password:
                    request.session['is_login'] =  True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
                    return redirect('/login/index/')
                else:
                    message = "密码不正确！"
            except:
                message = "用户不存在！"
        return render(request, 'login/login.html', locals())
    form = UserForm()
    return render(request, 'login/login.html', locals())

def register(request):
    if request.session.get("is_login", None):
        #已经登录，不允许注册
        return redirect("/login/index/")
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():
            username = register_form.cleaned_data["username"]
            password1 = register_form.cleaned_data["password1"]
            password2 = register_form.cleaned_data["password2"]
            email = register_form.cleaned_data["email"]
            sex = register_form.cleaned_data["sex"]
            if password1 != password2:
                message = "两次输入的密码不同"
                return render(request, 'login/register.html',locals())
            else:
                same_name_user = User.objects.filter(name=username)
                if same_name_user:
                    message = "用户已经存在，请重新选择用户名"
                    return render(request, 'login/register.html', locals())
                same_email_user =  User.objects.filter(email=email)
                if same_email_user:
                    message = "该邮箱地址已被注册，请使用别的邮箱!"
                    return render(request, 'login/register.html', locals())
                new_user = User.objects.create()
                new_user.name = username
                new_user.password = password1
                new_user.sex = sex
                new_user.email = email
                new_user.save()
                return redirect('/login/login/')
    register_form =  RegisterForm()
    print("init register_form")
    return render(request, 'login/register.html',locals())
def logout(request):
    if not request.session.get('is_login', None):
        return redirect("/login/index/")
    request.session.flush()
    return redirect("/login/index/")