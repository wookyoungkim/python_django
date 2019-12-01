from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models


class Review(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)    #자동으로 시간 추가
    updated_at = models.DateTimeField(auto_now=True)


def __str__(self):
    return self.title

class Meta:
    ordering = ['-created_at']
