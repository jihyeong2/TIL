[TOC]

# Django ManyToMany

> 2020.10.04



## 1. ManyToManyField

> M:N관계를 나타내기 위해 사용하는 필드로 다대다 관계로 설정할 모델 클래스가 필요하다.



### 1.1 데이터베이스

- Django에서는 다대다 관계를 나타내기 위해 중개 테이블을 자체적으로 만들어서 데이터베이스에 저장한다.
- 테이블 이름은 `AppName_ModelName_FieldName`으로 생성된다.
- `db_table` 옵션을 사용하여 테이블의 이름을 변경할 수도 있다.



### 1.2 Arguments

- `related_name`

  - 역참조할 때 사용할 변수이름이다. 이를 사용하지 않으면 `ModelName_set`을 통해 역참조할 수 있다. 하지만 참조하는 필드가 여러 개라면 중복될 수 있기 때문에 `related_name`을 설정해줘야 한다.

- `through`

  - Django Project에서는 중개 테이블을 자동으로 생성한다. 자동으로 생성된 테이블은 참조하는 테이블의 id와 참조되는 테이블의 id를 필드로 갖는다. 
  - 이외의 추가 데이터를 다대다 관계와 연결하려는 경우에는 직접 중개 테이블을 만들어서 `through` 옵션을 통해 설정할 수 있다.

- `symmetrical`

  - ManyToManyField가 동일한 모델을 가리키는 경우에 사용한다. 

  ```python
  from django.db import models
  
  class Person(models.Model):
      friends = models.ManyToManyField('self')
  ```

  - 위와 같이 선언하면 `person_set`으로 역참조가 불가능하다. 그렇기 때문에 `related_name`을 설정해주어야 한다.
  - 대신 `symmetrical= True`로, source 인스턴스가 target 인스턴스를 참조하면 target 인스턴스도 source 인스턴스를 참조하게 된다. (어떤 user를 follow하면 내가 참조하는 followings도 늘고 follow한 user의 followings도 늘게 된다.)
  - 대칭을 원치 않으면 `symmetrical=False`로 설정하면 된다.



### 1.3 중개 테이블 규칙

- source model과 target model이 다른 경우
  - id
  - <containing_model>_id
  - <other_model>_id
- ManyToManyField가 동일한 모델을 가리키는 경우
  - id
  - from_<model> _id
  - to_ <model>_id



## 2. Like

> `user`는 여러 `article`에 좋아요를 누를 수 있고
>
> `article`은 여러 `user`로부터 좋아요를 받을 수 있다.



### 2.1 Modeling

- 다대다 관계이므로 `ManyToManyField`를 사용해야 한다. `article`에 좋아요 버튼이 있고, 누를 경우 `article`에 `user`를 추가하도록 하기 위해 `article`에 필드를 선언한다.

```python
# article.model.py

class Article(models.Model):
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='like_articles')
```

- 이전에 `article`을 작성한 `user`를 참조하도록 하는 `ForeignKeyField`를 만들어줬기 때문에 `article_set`을 사용했을 때 혼동이 올 수 있기 때문에 `related_name`이 필수적이다.
- `user.article_set.all()` : 유저가 작성한 모든 article
- `user.like_articles.all()` : 유저가 좋아요한 모든 article



### 2.2 path

```python
# articles/urls.py
urlpattern=[
    path('<int:article_pk>/like/', views.like, name='like'),
]
```



### 2.3 views

```python
# articles/views.py

@require_POST
def like(request,article_pk):
    if request.user.is_authenticated:
        article=get_object_or_404(Article,pk=article_pk)
        user=request.user
        if article.like_users.filter(pk=user.pk).exists():
            article.like_user.remove(user)
        else:
            article.like_user.add(user)
        return redirect('articles:index')
    return redirect('accounts:login')
```

- 따로 rendering 해야 하는 html이 없고, DB에 변동을 가져오기 때문에 `POST` 방식만을 요구하며, 로그인 된 유저에게만 작동해야한다.
- 만약, 해당 유저가 이미 좋아요를 눌렀다면, 해당 유저를 좋아요한 `user`목록에서 제거하고, 그렇지 않으면 추가해야한다.
- `filter()` : 괄호 안에 적힌 조건에 맞는 데이터들을 쿼리 셋에 담아 가져온다.
- `exists()` : 최소한 하나의 레코드가 존재하는지의 여부를 알려준다.
- `.get()`을 쓰지 않고 `.filter()`를 사용한 이유는 `.get()`의 경우는 조건에 맞지 않으면 `DoesNotExist error`가 발생하기 때문에 무조건적으로 존재하는 값에 접근할 때 사용해야 한다. 하지만 이 상황의 경우는 존재하는지 여부를 모르고 없을 경우도 존재하기 때문에 `.filter()`를 사용해야 한다. `.filter()`는 조건에 맞지 않으면 빈 쿼리셋을 반환하기 때문에 `DoesNotExist error`가 발생하지 않는다.



### 2.4 html

```django
<!--articles/index.html-->

{% extends 'base.html' %}
{% block content %}
	<form action="{% url 'articles:like' article.pk %}" method="POST">
    	{% csrf_token %}
        {% if user in article.like_users.all %}
        	<button>좋아요 취소</button>
        {% else %}
        	<button>좋아요</button>
        {% endif %}
	</form>
	<p>{{article.like_users.all | length }} 명이 이 글을 좋아합니다.</p>
{% endblock %}
```



# 3. Follow

> `user`가 다른 `user`를 follow할 수 있으며, 둘 사이의 관계는 대칭적이지 않다.



### 3.1 Modeling

```python
# accounts/models.py

from django.conf import settings

class User(AbstractUser):
    followings=models.ManyToManyField('self', symmetrical=False,related_name='followers')
```

- 재귀적 참조가 이루어지고, 둘 사이의 관계는 대칭적이지 않다. 또한, 재귀적 참조일 경우 `User_set` 매니저를 사용할 수 없기 때문에 `related_name`옵션을 필수로 추가해주어야 한다.



### 3.2 path

```python
# articles/urls.py
urlpattern=[
    path('follow/<int:user_pk>/', views.follow, name='follow'),
]
```



### 3.3 views

```python
@require_POST
def follow(request,user_pk):
    if request.user.is_authenticated:
        you=get_object_or_404(get_user_model(),pk=user_pk)
        me=request.user
        if me != you:
            if you.followers.filter(pk=me.pk).exists():
                you.followers.remove(me)
            else :
                you.followers.add(me)
    return redirect('accounts:profile',you.username)
```



## 4.Profile

> 유저의 팔로윙 수와 팔로워 수, 유저가 쓴 게시글/댓글, 유저가 좋아요한 게시글들을 보여준다.



### 4.1 path

```python
# accounts/urls.py
urlpattern=[
    path('<username>/', views.profile, name='profile'),
]
```



### 4.2 views

```python
# accounts/views.py

def profile(request,username):
    person=get_object_or_404(get_user_model(), username=username)
    context={
        'person':person,
    }
    return render(request,'accounts/profile.html', context)
```



### 4.3 html

```django
<!-- accounts/profile.html -->

{% extends 'base.html' %}
{% block content %}
<h1 class="text-center">{{person.username}}의 프로필</h1>
<hr>
<!-- 팔로우/언팔로우 수,버튼-->
{% include 'accounts/_follow.html'%}
<hr>
<h2>{{person.username}}이 작성한 게시글</h2>
{% for article in person.article_set.all %}
    <div>{{article.title}}</div>
{% endfor %}
<hr>
<h2>{{person.username}}이 작성한 댓글글</h2>
{% for comment in person.comment_set.all %}
    <div>{{comment.content}}</div>
{% endfor %}
<hr>
<h2>{{person.username}}이 작성한 좋아요 한 게시글</h2>
{% for article in person.like_articles.all %}
    <div>{{article.title}}</div>
{% endfor %}
<hr>
<a href="{% url 'articles:index' %}">[BACK]</a>
{% endblock  %}
```

- `include` : 특정 내용만을 담당하거나, 다른 페이지에서도 두루 쓰일 부분을 다른 템플릿으로 분할하여 놓고, `include`를 통해 사용할 수 있다.



```django
<!-- accounts/_follow.html -->

<div class="jumbotron">
  {% with followers=person.followers.all followings=person.followings.all %}
    <p class="lead">
      팔로워 수 : {{ followers|length }} / 팔로잉 수 : {{ followings|length }} 
    </p>
    <!-- 팔로우 버튼 / 언팔로우 버튼 -->
    {% if request.user != person %}
      <form action="{% url 'accounts:follow' person.pk %}" method="POST">
        {% csrf_token %}
        {% if request.user in followers %}
          <button class="btn btn-secondary">Unfollow</button>
        {% else %}
          <button class="btn btn-primary">Follow</button>
        {% endif %}
      </form>
    {% endif %}
  {% endwith %}
</div>
```

- `with` : 한 페이지 내에서 반복적으로 쓰이는 복잡한 변수를 간단한 이름으로 바꾸어서 사용하도록 하는 태그이다. `{% with %}` 와 `{% endwith %}` 사이에서만 사용 가능하다.