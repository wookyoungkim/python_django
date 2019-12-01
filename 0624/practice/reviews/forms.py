from django import forms
from .models import Review

# Model을 기반으로 한 Form
class ReviewForm(forms.ModelForm):
    class Meta:     #부가정보 (주된 정보는 x)
        model = Review
        fields = ['title', 'text']