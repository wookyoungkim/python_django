from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.

def home(request):
    blogs=Blog.objects      #admin에서 확인한 blog안의 데이터
    return render(request, 'home.html', {'blogs':blogs})

def detail(request, blog_id):
    blog_detail=get_object_or_404(Blog, pk=blog_id)
    return render(request,'detail.html',{'blog':blog_detail})