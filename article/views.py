from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Article, Category, Tag, Comment
from .forms import ArticleForm
from .forms import CommentForm
# Create your views here.

def articleList(request):
    categories = Category.objects.all()
    articles = Article.objects.all().prefetch_related('tags')
    return render(request, 'index.html', {"articles": articles, "categories": categories})


def articleCatList(request, pk):
    categories = Category.objects.all()
    articles = Article.objects.filter(category_id=pk).prefetch_related('tags')
    return render(request, 'index.html', {"articles": articles, "categories": categories})

def newArticle(request):
    form = ArticleForm()
    return render(request, 'new_article.html', {"form": form})


def addArticle(request):
    form = ArticleForm(request.POST, request.FILES)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        return HttpResponseRedirect('/')

    return render(request, 'new_article.html', {"form": form})


def deleteArticle(request, pk):
    Article.objects.get(pk=pk).delete()
    return HttpResponseRedirect('/')

def editFormArticle(request, pk):
    article = Article.objects.get(pk=pk)
    form = ArticleForm(instance=article)
    return render(request, 'edit_article.html', {"form": form, "pk":pk})


def editArticle(request, pk):
    article = Article.objects.get(pk=pk)
    form = ArticleForm(request.POST, instance=article)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')

    return render(request, 'new_article.html', {"form": form})

def pr_details(request, pk):
    categories = Category.objects.all()
    articles = Article.objects.filter(id=pk).prefetch_related('tags')
    return render(request, 'pr_details.html', {"articles": articles, "categories": categories})




def comment(request):
    form = CommentForm()
    return render(request, 'pr_details.html', {"form": form})


def commentEdit(request):
    form = CommentForm(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')

    return render(request, 'pr_details.html', {"form": form})


