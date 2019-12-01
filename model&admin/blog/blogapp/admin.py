from django.contrib import admin
from .models import Blog    #같은 폴더위치에 있는 model파일에서 Blog클래스 갖고와라

# Register your models here.

admin.site.register(Blog)       #admin이라는 site에 BLog라는 클래스 등록해라