from django import forms
from .models import Article, News


class AddArticle(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['image']


class AddNews(forms.ModelForm):
    class Meta:
        model = News
        fields = ['image']
