# CSS

> HTML과 별개의 언어로써, HTML의 Style을 설정하는 언어이다.
>
> 스타일, 레이아웃 등을 통해 HTML이 사용자에게 어떻게 표시 되는지를 지정하는 언어



### CSS구문

- 특정 Style을 설정할 Selector를 먼저 선언한다. 해당 Selector 전체에 Style을 부여하고 싶으면 뒤에 Element를 생략하고, 특정 Element에만 부여하고 싶으면 원하는 Element를 같이 선언한다.
- 중괄호 안에는 부여할 스타일을 Property:Value; 형식으로 선언한다. 



##### 선언문

- Property(속성) : Element가 갖고 있는 특징으로 가령, 배경색이나 글씨색, 글씨크기 등이 Property이다.
- Value(값)  : 각 속성에 값을 부여하며, 글꼴이나 배경색의 스타일 값을 나타낸다.



##### CSS 정의 방법

- Inline style
- 내부 참조(Embedding style)
- 외부 참조(Link style)



### CSS Selector

> 선택자는 스타일을 지정할 웹 페이지의 HTML 요소를 대상으로 하는 데 사용



##### Class Selector

- `.` 문자로 시작하며, 해당 클래스를 속성으로 갖는 Element 모든 항목을 선택한다.

##### Id Selector

- Id Selector `#` 문자로 시작하며, 기본적으로 Class Selector와 같은 방식으로 사용
- Id는 Selector 우선순위가 높아서 여러 태그에 동시에 사용하면 프로그램이 꼬일 수 있으므로, 신중하게 사용해야 한다.

##### 적용 우선순위

1. !important
   - Selector 중 가장 우선 순위가 높다. 정상적인 cascading을 벗어나는 방식으로, 반드시 필요한 경우가 아니면 사용하지 않는 것이 좋다.
2. Inline Style
   - HTML 문서 내의 Element Tag에 style 속성을 직접 부여하는 방식이다.
3. Id Selector
   - 보통 사용하는 class selector보다 우선순위가 높으므로 다루기가 어렵다.
   - 문서 내 `링크이동`이나 `for`를 사용하는 특별한 경우에만 아이디를 사용한다.
4. Class Selector
5. Element Selector
6. Source Sequence



### CSS 단위



##### px

- 모니터 해상도의 한 화소인 '픽셀'을 기준
- 픽셀 크기는 변하지 않으므로 고정적이다.



##### %

- 백분율 단위
- 가변적인 레이아웃에서 자주 사용



##### em

- em은 상속의 영향을 받으며, 부모 요소의 size를 기준으로 크기를 계산한다.



##### rem

- 최상위 요소인 html을 절대 단위를 기준으로 크기를 계산한다.

- 상속에 영향을 받지 않기 때문에 대부분의 경우 `rem`을 많이 사용한다.



##### viewport

- 각 스마트폰이나 태블릿 디바이스 화면을 일컫는 용어로 사용되며, viewport를 기준으로 한 상대적인 사이즈를 조절하고 싶을 때 사용한다.
- vw,vh



##### 색상 표현 단위

1. 색상 키워드
   - 색상 키워드는 대소문자를 구분하지 않는 식별자로 red,blue,black처럼 특정 색을 나타낸다.
2. RGB 색상
   - RGB의 비율을 16진수로 표기하여 특정 색을 표현
   - a는 alpha(투명도)가 추가된 것
3. HSL 색상
   - 색상,채도,명도를 통해 특정 색상을 표현
   - a는 alpha(투명도)가 추가된 것



### Box Model

> 웹 디자인은 contents를 담을 box model을 정의하고 CSS 속성을 통해 스타일과 위치 및 정렬을 지정하는 것.

- 모든 HTML 요소는 box형태로 되어 있다.
- 하나의 박스는 네 영역으로 이루어진다.
  - content / padding / border / margin

1.  Content
   - 글이나 이미지, 비디오 등 요소의 실제 내용
2. Padding(안쪽 여백)
   - Border(테두리) 안쪽의 내부 여백
   - 배경색, 이미지 지정 가능
3. Border
4. Margin
   - 테두리 바깥의 외부 여백
   - 배경색 지정 불가



##### 마진 상쇄

- block의 top 및 bottom margin이 때로는 가장 큰 한 마진으로 결합된다.



### Display

> Display CSS 속성은 요소를 블록과 인라인 요소 중 어느 쪽으로 처리할지와 함께 자식 요소를 배치할 때 사용할 레이아웃을 설정한다.



##### block

- 요소는 블록 요소 상자를 생성하여 일반 흐름에서 요소 앞뒤에 줄 바꿈을 생성한다.
- 블록 레벨 요소 안에 인라인 레벨 요소가 들어갈 수 있다.



##### inline

- 줄바꿈이 일어나지 않는 행의 일부 요소
- content 너비만큼 가로 폭을 차지
- width, height, margin-top, margin-bottom을 지정할 수 없음
- 상하 여백은 line-height로 지정



##### inline-block

- inline처럼 텍스트 흐름대로 나열, block처럼 박스 형태이기 때문에 block 속성 사용가능.



##### none

- 해당 요소를 화면에서 사라지게 하며, 요쇼의 공간조차 사라지게 한다.
- `visibility: hidden;`은 해당 요소를 화면에서 사라지게는 하지만, 공간 자체가 사라지지는 않는다.



### Position

##### 박스의 위치 속성 & 값

- position
  - static / absolute / relative / fixed
  - z-index

##### 기본 개념

1. static(기본 위치)
   - 모든 태그의 기본
   - 태그의 default 값
2. relative(상대 위치)
   - 기본 위치(static)를 기준으로 좌표 속성을 사용해 위치 이동
3. absolute(절대 위치)
   - static이 아닌 부모/조상 요소를 기준으로 좌표 속성만큼 이동
   - 부모 요소를 찾아가고 나아가 없다면 body에 붙는다.
4. fixed(고정 위치)
   - 부모 요소와 관계없이 viewport를 기준으로 좌표 속성만큼 이동하며, 스크롤을 내리거나 올려도 항상 같은 곳에 위치한다.



##### absolute

- `absolute`는 원래 위치해 있었던 과거 위치에 있던 공간은 더 이상 존재하지 않는다는 점이 특징이다.
- 즉, 다른 모든 것과는 별개로 독자적인 곳에 놓이게 된다.
- When do you use?
  - 페이지의 다른 요소의 위치와 간섭하지 않는 격리된 사용자 인터페이스 기능을 만들 수 있다.
  - 팝업 정보 상자 및 제어메뉴, 롤오버 패널, 페이지 어느 곳에서나 끌어서 놓기할 수 있는 유저 인터페이스 페이지 등