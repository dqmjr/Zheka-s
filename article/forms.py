from django import forms
from .models import Article
from .models import Comment

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ('author',)
        fields = ['title', 'description', 'tags', 'category', 'image']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['user', 'email','body']
