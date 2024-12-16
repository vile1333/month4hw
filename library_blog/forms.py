from django import forms
from library_blog.models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text_review','stars']