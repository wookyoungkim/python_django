from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<int:post_id>', views.detail, name="detail"),
    path('new/', views.new, name="new"),
    path('create', views.create, name="create"),      
     #path를 한줄 추가한다고 무조건 html로드하는것은 아님-> path의 두번째 인자 view는 views.py의 create함수 호출하라는 뜻
    path('<int:blog_id>/delete', views.delete, name='post_delete')

]
