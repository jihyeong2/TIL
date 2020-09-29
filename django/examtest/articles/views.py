from django.shortcuts import render,redirect,get_object_or_404
from django.views.decorators.http import require_http_methods,require_POST
from django.contrib.auth.decorators import login_required
from .models import Comment,Article
from .forms import ArticleForm,CommentForm

# Create your views here.
def index(request):
    articles=Article.objects.order_by('-pk')
    context={
        'articles':articles,
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


@login_required
@require_http_methods(['GET','POST'])
def update(request,pk):
    article=get_object_or_404(Article,pk=pk)
    if request.user == article.user:
        if request.method=='POST':
            form=ArticleForm(request.POST, instance=article)
            if form.is_valid():
                form.save()
                return redirect('articles:detail', article.pk)
        else:
            form=ArticleForm(instance=article)
    else:
        return redirect('articles:index')
    context={
        'form':form,
        'article':article,
    }
    return render(request,'articles/update.html', context)


def detail(request,pk):
    article=get_object_or_404(Article,pk=pk)
    comments=article.comments.all()
    form=CommentForm()
    context={
        'article':article,
        'comments':comments,
        'form':form,
    }
    return render(request, 'articles/detail.html', context)

@require_POST
def delete(request,pk):
    if request.user.is_authenticated:
        article=get_object_or_404(Article,pk=pk)
        if request.user==article.user:
            article.delete()
        return redirect('articles:index')
    return redirect('articles:detail', article.pk)



@require_POST
def comment_create(request,article_pk):
    if request.user.is_authenticated:
        article=get_object_or_404(Article,pk=article_pk)
        form=CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.user=request.user
            comment.article=article
            comment.save()
            return redirect('articles:detail', article_pk)
        context={
            'article':article,
            'form':form,
        }
        return render(request,'articles/detail.html', context)
    return redirect('accounts:login')


@require_POST
def comment_delete(request,article_pk,comment_pk):
    if request.user.is_authenticated:
        comment=get_object_or_404(Comment,pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
    return redirect('articles:detail', article_pk)