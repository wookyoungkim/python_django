from django.conf import settings
from django.contrib import auth
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.utils import timezone
from blogapp.models import Blog, User
from django.contrib.auth.decorators import login_required


# Create your views here.
# 로그인
def login(request):
    if request.method == 'GET':
        error_message = '로그인페이지입니다.'
        return render(request, 'login.html', {'error_message':error_message})
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)        
        if user is not None:
            auth.login(request, user)
            return render(request, 'users_home.html', {'user':user})
    error_message = '잘못된 요청입니다. 다시 로그인해주세요.'  
    return render(request, 'login.html', {'error_message':error_message})
        
@login_required
def logout(request):
    auth.logout(request)
    return redirect('users/')

# 회원가입
def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                username=request.POST['username'],
                name=request.POST.get('name'), 
                password=request.POST['password1'], 
                age=request.POST['age'],
                gender=request.POST['gender'], 
                )
            if user is not None:
                auth.login(request, user)
                return redirect('users/')
    print("회원가입 안됨")
    return render(request, 'signup.html') 

def home(request):
    blogs=Blog.objects
    return render(request,'home.html',{'blogs':blogs})

def detail(request, blog_id):       #마이페이지랑 똑같
    user=requesr.user
    blog_detail=get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html',{'blog':blog_detail, 'user':user})

def new(request):
    return render(request, 'new.html')

def create(request):    #입력받은 내용 디비에 넣어주기
    blog=Blog()
    blog.title=request.GET['title'] #html from태그 안
    blog.body=request.GET['body']
    blog.pub_date=timezone.datetime.now()   #입력한 시간 자동으로 넘어가게끔 
    blog.save()     #db에 저장하려면
    return redirect('/blog/'+str(post.id))  #요청 처리하고 보여주는 페이지 -> render: 요청 들어오면 이 html 파일 보여주기, redirect: 요청 들어오면 저쪽 url로 보내기 

def delete(request, post_id):
    user=request.user
    blog_delete=get_object_or_404(Blog, id=post_id)
    blog_delete.delete()
    return redirect('/blogapp/home')   #내가 받은 ㅁ세지 삭제