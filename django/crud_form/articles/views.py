from django.shortcuts import render,redirect
from django.views.decorators.http import require_POST
from .models import Article
from .forms import ArticleForm
# Create your views here.
def index(request):
    # 모든 articles를 보여준다.
    articles=Article.objects.all()
    context={
        'articles':articles,
    }
    return render(request,'articles/index.html',context)


def create(request):
    # 쓸 수 있는 페이지를 보여주고
    # 받은 데이터를 DB에 저장
    if request.method=="POST":
        form = ArticleForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            article = form.save() #form을 통해 저장하고 return값이 생김.
            return redirect('articles:detail',article.pk)
    else:    
        form = ArticleForm()
    context={
        'form':form
    }
    return render(request,'articles/create.html',context)


def detail(request,article_pk): #urls에서 동적라우팅으로 선언한 변수와 동일해야함.
    article = Article.objects.get(pk=article_pk)
    context={
        'article':article,
    }
    return render(request,'articles/detail.html',context)


def update(request,article_pk):
    # 업데이트 할 수 있는 페이지 보여줌
    # 업데이트 수행
    article = Article.objects.get(pk=article_pk)
    if request.method=="POST":
        form=ArticleForm(data=request.POST, instance=article, files=request.FILES)
        if form.is_valid():
            article=form.save()
            return redirect('articles:detail',article.pk)
    else:
        form = ArticleForm(instance=article)
    context={
        'form':form,
        'article':article,
    }
    return render(request,'articles/update.html',context)

@require_POST # decorator 아래에 있는 함수를 꾸며주는 효과
# request의 method가 POST가 아니면 아예 함수가 실행되지 않음
def delete(requet,article_pk):
    article=Article.objects.get(pk=article_pk)
    article.delete()
    return redirect('articles:index')