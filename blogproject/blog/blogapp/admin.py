from django.contrib import admin
from .models import User, Blog   #같은 폴더 내의 모델스에서 블로그 클래스 가져오기

# Register your models here.

admin.site.register(User)
admin.site.register(Blog)
