from django.shortcuts import render,redirect,get_object_or_404
from .forms import ArticleForm
from .models import Article
from django.views.decorators.http import require_http_methods, require_POST
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    articles=Article.objects.order_by('-pk')
    context={
        'articles':articles
    }
    return render(request,'articles/index.html', context)

@require_http_methods(['GET','POST'])
def create(request):
    if request.method=='POST':
        form=ArticleForm(request.POST)
        if form.is_valid():
            article=form.save()
            return redirect('articles:detail' ,article.pk)
    else:
        form=ArticleForm()
    context={
        'form':form,
    }
    return render(request,'articles/create.html',context)


def detail(request,pk):
    article=get_object_or_404(Article,pk=pk)
    context={
        'article':article,
    }
    return render(request,'articles/detail.html', context)


@require_http_methods(['GET','POST'])
def update(request,pk):
    article=Article.objects.get(pk=pk)
    if request.method=='POST':
        form=ArticleForm(request.POST,instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form=ArticleForm(instance=article)
    context={
        'form':form,
    }
    return render(request,'articles/create.html', context)


@require_POST
def delete(request,pk):
    article=Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')