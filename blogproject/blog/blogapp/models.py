from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    """ User Model """
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    profile_image = models.ImageField(
        upload_to='profile_images',
        blank=True,
        null=True, 
    )
    name = models.CharField(max_length=140, blank=False,null=True) # 유저 실명
    phone = models.CharField(max_length=225, blank=False,null=True) # 핸드폰 번호->논의 필요
    bio = models.TextField(blank=True, null=True)
    gender = models.CharField(max_length=80, choices=GENDER_CHOICES, null=True)
    profile_open = models.BooleanField(default=True)
    age = models.CharField(max_length=50, null=True)

class Blog(models.Model):
    title=models.CharField(max_length=200)
    pub_date=models.DateTimeField('date published')
    body=models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]