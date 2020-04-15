from django.shortcuts import render
from article.models import Article, Category
# Create your views here.


def profilePage(request):
    categories = Category.objects.all()
    articles = Article.objects.filter(author=request.user).prefetch_related('tags')
    return render(request, 'profile.html', {"articles": articles, "categories": categories})

    
