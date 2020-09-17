목차

[TOC]



​	

# Django

## Intro

### 설치

```bash
$ pip install django
```

- 특정 버전 설치

  ```bash
  $ pip install django==2.1.15
  ```

- 설치 확인

  ```bash
  $ pip list
  ```

  

### 프로젝트 생성

> project를 생성할 때, python이나 django에서 사용중인 이름 안됨. (`-`안됨)

```bash
$ django-admin startproject first_project
```

### 서버 실행

```bash
$ python manage.py runserver
```

### 프로젝트 구조

- `__init__.py`
  - python에게 이 디렉토리를 하나의 python 패키지로 다루도록 지시하는 파일
- `settings.py`
  - 사용하려는 app을 등록하거나, static files의 위치, database 세부 설정 등을 작성하는 파일
- `urls.py`
  - 사이트의 url과 view의 연결을 지정
- `wsgi.py`
  - django application이 web server와 연결 및 소통하는 것을 도움.
- `asgi.py`
  - django application이 비동기식 web server와 연결 및 소통하는 것을 도움.

### Application(app)

- 프로젝트는 어플리케이션의 집합이며, 실제로 data를 처리하고 페이지를 보여주는 역할
- 프로젝트는 여러 개의 어플리케이션을 포함할 수 있으며, 기능 단위로 쪼개는 것이 일반적
- 일반적으로 app 이름은 복수형으로 하는 것이 좋다.

```bash
$ python manage.py startapp articles
```

### Application 구조

- `admin.py`
  - 관리자용 페이지 관련 기능을 작성하는 파일
- `apps.py`
  - 앱의 정보가 있지만, 직접 수정할 일은 없다.
- `models.py`
  - 앱에서 사용하는 Model(Database)를 정의하는 파일

- `tests.py`
  - 테스트 코드를 작성하는 파일
- `views.py`
  - view가 정의되는 파일

### Application 등록

- 생성한 app은 `settings.py`에 등록을 시켜야 함. 

```python
# settings.py

INSTALLED_APPS = [
	'articles',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

### Internationalization

- `settings.py`의 LANGUAGE_CODE와 TIME_ZONE을 변경하여, 언어와 시간을 원하는 대로 설정할 수 있다.

```PYTHON
# settings.py

LANGUAGE_CODE = 'ko-kr'
TIME_ZONE = 'Asia/Seoul'
```

### runserver(Automatic reloading)

- 개발 서버는 매 요청마다 자동으로 python 코드를 다시 불러온다.
- 코드의 변경사항을 반영하기 위해 서버를 재가동하지 않아도 된다.



## URL & Template

### urls.py

- 장고 서버로 요청이 들어오면, 어디로 가야하는지 인식하고 그와 관련된 view로 넘겨준다.

- `views.py`에서 만든 함수를 연결시켜준다.

  ```python
  from django.urls import path
  from articles import views
  urlpatterns=[
      path('index',views.index,name='index')
  ]
  ```

  

### views.py

- Model과 Template 사이를 연결해주는 다리 역할을 하며, views에서는 서버로 저장될 입력 데이터를 저장하기도 하고 서버의 데이터를 Template으로 전달하여 사용자들로 하여금 보여주도록한다.

```python
def index(request):
    return render(request,'index.html')
```

### Templates

- Django에서 template이라 부르는 HTML 파일은 기본적으로 app 폴더 안의 templates 폴더 안에 위치한다. 
- 여러 개의 app이 있을 때는 각 app의 urls에 app_name을 설정해주고, templates안에 app_name으로 폴더를 생성한 후 app_name 폴더 안에 HTML 파일을 위치시킨다. 다른 페이지에서 이동하고자 할 때에는 {% url 'articles:index' %}와 같은 형식으로 이동한다.

### Template Variable

- `render()`를 사용하여 views.py에서 정의한 변수를 template 파일로 넘겨 사용하는 것.
- `render()`의 세번째 인자로 Dict type으로 넘겨준다. render에서 넘길 때의 key는 template에서 변수처럼 사용할 수 있으며 {{ ____ }} 괄호 안에 기입하여 표현한다.

### Variable Routing

> 주소를 변수처럼 사용하여 동적으로 주소를 만드는 방법

```python
urlpatterns=[
    path('hello/<str:name>/', views.hello),
]
```

```python
def hello(request,name):
    context={
        'name':name
    }
    return render(request,'hello.html',context)
```

```html
<h1>안녕! {{name}}</h1>
```



## HTML Form

### From

- 웹에서 사용자의 정보를 입력하는 text,button,checkbox,file,hidden,image,password,radio,reset,submit의 방식을 제공하고, 그 데이터를 서버로 전송하는 역할을 담당하는 HTML Tag
- form은 다른 페이지로 데이터를 전달하기 위해 사용한다.
- 핵심 속성 2가지
  - action : 데이터가 전송될 URL
  - method : 데이터 전달 방식

### Input

- 데이터를 입력 받기 위해 사용되는 가장 중요한 태그
- input 태그의 속성
  - `name`
    - action에서 지정한 URL로 데이터를 넘겼을 때 해당 URL에서 name을 key로 사용하여 변수에 접근할 수 있다.
    - GET/POST 방식으로 서버에 전달할 수 있고, `?key=value&key=value`형태로 전달된다.

### HTTP method `GET`

- 서버로부터 정보를 조회하는 데 사용하며, 쿼리 스트링을 통해 전송한다.
- 서버의 데이터나 상태를 변경시키지 않아야 하기 때문에 조회할 때 사용한다.
- 서버에 요청하면 HTML 문서를 받는데 이 때 사용하는 요청의 방식이 GET 방식이다.

### Request

- 요청 간의 모든 정보를 담고 있는 변수
- 페이지가 요청되면 Django는 요청에 대한 메타 데이터를 포함하는 HttpRequest 객체를 만든다.



-------------------

settings.py안에 있는 TEMPLATES context_processors의 auth가 기본적으로 내장되어 있기 때문에 base.html에서 받는 context가 없어도 user를 바로 사용할 수 있음.



회원가입 > user create

로그인 > session_id create > login 함수(request와 user 두 가지를 인자로 넘겨줘야함.)

로그아웃 > session_id delete > logout 함수(request만 인자로 넘기면 됨)

회원탈퇴 > user delete

