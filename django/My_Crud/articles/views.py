from .models import Article
from .forms import ArticleForm
from django.shortcuts import render,redirect,get_object_or_404
from django.views.decorators.http import require_http_methods,require_POST

def index(request):
    # db에 저장되어 있는 모든 article들 보여주기
    articles=Article.objects.order_by('-pk')
    context={
        'articles':articles,
    }
    return render(request,'articles/index.html',context)

@require_http_methods(['GET','POST'])
def create(request):
    # 게시글 생성 페이지 보여주기
    # 게시글 db에 등록하기
    if request.method=='POST':
        form=ArticleForm(data=request.POST)
        if form.is_valid():
            article=form.save()
            return redirect('articles:detail', article.pk)
    else:
        form=ArticleForm()
    context={
        'form':form,
    }
    return render(request,'articles/create.html',context)


def detail(request,article_pk):
    article=get_object_or_404(Article,pk=article_pk)
    context={
        'article':article,
    }
    return render(request,'articles/detail.html',context)

@require_http_methods(['GET','POST'])
def update(request,article_pk):
    article=get_object_or_404(Article,pk=article_pk)
    if request.method=='POST':
        form=ArticleForm(data=request.POST,instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form=ArticleForm(instance=article)
    context={
        'form':form,
        'article':article,
    }
    return render(request,'articles/create.html',context)


@require_POST
def delete(request,article_pk):
    article=get_object_or_404(Article,pk=article_pk)
    article.delete()
    return redirect('articles:index')