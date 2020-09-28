from django.shortcuts import render,redirect,get_object_or_404
from django.views.decorators.http import require_http_methods,require_POST
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    articles=Article.objects.order_by('-pk')
    context={
        'articles':articles
    }
    return render(request,'articles/index.html', context)

@login_required
@require_http_methods(['GET','POST'])
def create(request):
    if request.method=='POST':
        form=ArticleForm(request.POST)
        if form.is_valid():
            article=form.save(commit=False)
            article.user=request.user
            article.save()
            return redirect('articles:detail', article.pk)
    else:
        form=ArticleForm()
    context={
        'form':form,
    }
    return render(request,'articles/create.html',context)


def detail(request,pk):
    article=Article.objects.get(pk=pk)
    form=CommentForm()
    context={
        'article':article,
        'form':form,
    }
    return render(request,'articles/detail.html',context)

@require_http_methods(['GET','POST'])
def update(request,pk):
    article=get_object_or_404(Article,pk=pk)
    if request.user==article.user:
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
        return render(request, 'articles/create.html',context)
    return redirect('articles:detail',article.pk)


@require_POST
def delete(request,pk):
    article=Article.objects.get(pk=pk)
    if request.user==article.user:
        article.delete()
    return redirect('articles:index')


@require_POST
def comment_create(request,article_pk):
    if request.user.is_authenticated:
        article=get_object_or_404(Article,pk=article_pk)
        comment_form=CommentForm(request.POST)
        if comment_form.is_valid():
            comment=comment_form.save(commit=False)
            comment.article=article
            comment.user=request.user
            comment_form.save()
            return redirect('articles:detail',article.pk)
        context={
            'article':article,
            'comment_form':comment_form,
        }
        return render(request,'articles/detail.html', context)
    return redirect('accounts:login')



@require_POST
def comment_delete(request,article_pk,comment_pk):
    comment=get_object_or_404(Comment,pk=comment_pk)
    if request.user==comment.user:
        comment.delete()
    return redirect('articles:detail', article_pk)