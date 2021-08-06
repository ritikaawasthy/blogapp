from django.shortcuts import render
from .forms import UserRegisterForm, ExtendedUserForm, BlogForm
from django.http import QueryDict
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import ExtendedUser, Blog
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
# Create your views here.
def loginView(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        data= request.POST
        username = request.POST['username']
        password = request.POST['password1']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = login(request, user)
            print(request.user)
            userobj= ExtendedUser.objects.get(user=request.user)
            print(userobj)
            numLogin= 1#userobj[0]['noOfLogin']
            userobj.noOfLogin= numLogin+1
            userobj.save()
            print(ExtendedUser.objects.filter(user=request.user).values())
            #return render(request,'home.html')
            return redirect("home")
        else:
            data="Invalid Credentials"
            return render(request, 'login.html', {"data": data})

#function for logout
def logoutView(request):
    logout(request)
    #return render(request,'home.html')
    return redirect("home")

#function for signup
def signUpView(request):
    if request.method=='GET':
        return render(request, 'signUp.html')
    if request.method=='POST':
        data= request.POST
        username= data['username']
        dataEx=QueryDict('', mutable=True)
        form = UserRegisterForm(data)
        print(form.is_valid())
        if (form.is_valid()==True):
            form.save()
            userObj=User.objects.filter(username=username).values('id')
            user=userObj[0]['id']
            dataEx.update({'user':user })
            formEx= ExtendedUserForm(dataEx) 
            if(formEx.is_valid()==True):
                formEx.save()
                print(ExtendedUser.objects.filter(user=user).values())
                data="You have been successfully registered, please login"
                return render(request, 'login.html', {"data": data})
            else:
                data="Error"
                return render(request, 'signUp.html', {"data": data})
        else:
            data= form.errors
            print(form.errors)
            return render(request, 'signUp.html', {"data": data})

def home(request):
    if request.method=="GET":
        blogObj= Blog.objects.all()
        page = request.GET.get('page', 1)
        blogObjList=list(blogObj.values())
        paginator = Paginator(blogObjList,5 )
        try:
            blogList = paginator.page(page)
        except PageNotAnInteger:
            blogList = paginator.page(1)
        except EmptyPage:
            blogList = paginator.page(paginator.num_pages)
    return render(request, "home.html", {"blogList": blogList, "user": request.user})

@login_required(login_url='login/')
def addBlog(request):
    if request.method=='GET':
        return render(request, "blog.html")
    if request.method=='POST':
        datadict=QueryDict('', mutable=True)
        data=request.POST
        datadict.update({"user":request.user, "title": data['title'], "content": data['content'], "tag": data['tag'], "name": data['name']})
        print(datadict)
        form=BlogForm(datadict)
        if form.is_valid():
            form.save()
            data="Post created successfully"
        else:
            data= form.errors
        return render(request, "blog.html", {"data":data})
