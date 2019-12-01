from django.db import models

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=200)
    pub_date=models.DateTimeField('date published')
    body=models.TextField()

    def __str__(self):      #admin페이지에서 제목 나오게
        return self.title

    def summary(self):
        return self.body[:100]