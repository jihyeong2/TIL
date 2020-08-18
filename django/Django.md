# Django

### 1. Django 실행 순서

1. django 설치
2. django pjt 생성
3. runserver 후 로켓페이지 확인
4. django app 생성
5. app을 pjt에 등록
6. urls -> view



### 2. Django Template Language

> Django template system에서 사용하는 built-in template system이다.
>
> 조건, 반복, 치환, 필터, 변수 등의 기능을 제공한다.
>
> 프로그래밍적 로직이 아니라, 프레젠테이션을 표현하기 위한 것임.
>
> 파이썬처럼 if,for를 사용할 수 있지만, 단순히 python code로 실행되는 것은 아님.



- Syntax

  - variable : `{{}}`
  - filter : `{{variable|filter}}`
  - Tag : `{% Tag %}`
  - for :

  ```html
  {% for _ in list %}
  --> python에서의 for문과 동일하게 순회한다.
  {% empty %}
  --> 순회할 list가 비어있을 때 실행되는 부분이다.
  {% endfor %}
  --> for tag의 마지막을 나타내는 부분으로 꼭 같이 작성해야 한다.
  ```

  - if :

  ```html
  {% if condition %}
  {% else %}
  {% endif %}
  ```

  

### 3. 템플릿 시스템 설계 철학

- 장고는 템플릿 시스템의 표현을 제어하는 도구이자 표현에 관련된 로직일뿐이라고 생각한다.
- 템플릿 시스템에서는 이러한 기본 목표를 넘어서는 기능을 지원해서는 안된다.

