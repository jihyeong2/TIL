# Django Form

> HTML에서 form과 input을 통해 사용자의 데이터를 받았는데, 이러한 방식으로 데이터를 받으면 해야할 작업들이 많아짐. Django에서는 Form을 통해서 데이터를 입력받아 검증까지 할 수 있다.

## Form

> Form은 django 프로젝트의 유효성 검사 도구들 중 하나이며, 공격 및 데이터 손상에 대한 중요한 방어수단이다.
>
> 1. 렌더링을 위한 데이터 준비 및 재구성.
>
> 2. 데이터에 대한 HTML Forms생성
>
> 3. 클라이언트로부터 받은 데아터 수신 및 처리

- Form Class

  - django Form 관리 시스템의 핵심
  - Form내 field, field배치, 디스플레이 widget, label, 초기값, 유효하지 않는 field에 관련된 에러메세지를 결정한다.

  - forms.py를 생성해서 `CharField()`, `ChoiceField()`와 같이 데이터 필드 포함하는 class를 생성한다.
  - views.py에서 `from .forms import {클래스 명}` Form Class를 import한 후, 입력받을 html과 연동되는 함수에서 Form Class를 객체로 생성한 후 context로 html 페이지에 같이 render해준다.(render 인자에 context 추가)
  - 데이터를 입력받을 html 파일에서 {{form}}을 작성하면 label, input을 대신할 수 있다.
  - form.as_p : forms를 p tag 취급
  - from.as_table: forms를 table로 취급
  - form.as_ul : forms를 unordered list로 취급

  - Models.py에서 생성한 클래스와 forms.py에서 생성한 클래스가 중복되는 부분이 생김. 이를 방지하기 위해 ModelForm을 django에서 제공함.
  - forms.py에서 forms.ModelForm을 상속하는 클래스를 생성한 후 내부 메타 클래스를 생성한다. meta 클래스는 생성한 클래스의 필드를 포함한다.

- 