# CSS Layout

> 웹페이지에 포함되는 요소들을 어떻게 취합하고 그것들이 어느 위치에 놓일 것인지를 제어한다.

### Float

---

>한 요소(element)가 정상 흐름(normal flow)으로부터 빠져 텍스트 및 인라인(inline)요소가 그 주위를 감싸 자기 컨테이너의 좌,우측을 따라 배치되어야 함을 지정한다.



##### Clearfix

- float 요소와 다른 텍스트가 아닌 block 요소 간의 레이아웃 깨짐을 막기 위해 다음과 같이 작성한다.

```css
.clearfix::after{
	content: "";
	display: block;
	clear: both;
}
```



##### 정리

- flexbox 및 그리드 레이아웃과 같은 기술이 나오기 이전에 float는 열 레이아웃을 만드는데 사용되었다.
- mdn에서는 더 새롭고 나은 레이아웃 기술이 나와 있으므로 레거시 레이아웃 기술로 분류해놓기도 했다.
- 결국 원래 텍스트 블록 내에서 float 이미지를 위한 역할로 돌아간 것이다.

- 여전히 사용하는 경우도 있다.



### Flexbox

---

> 일명 Flexbox라 불리는 Flexible Box Module은 Flexbox 인터페이스 내의 아이템 간 공간 배분과 강력한 정렬 기능을 제공하기 위한 1차원 레이아웃 모델로 설계되었다.
>
> 웹페이지의 컨테이너에 아이템의 폭과 높이 또는 순서를 변경해서 웹페이지의 사용 가능한 공간을 최대한 채우고 이를 디바이스 종류에 따라 유연하게 반영하도록 하는 개념



##### 핵심 개념

- 요소
  - flex container
  - flex items
- 축
  - main axis(주축)
  - cross axis(교차축)



##### flex container

- flexbox 레이아웃을 형성하는 가장 기본적인 모델
- flexbox가 놓여있는 영역
- flex 컨테이너를 생성하려면 영역 내의 컨테이너 요소의 display 값을 flex 혹은 inline-flex로 지정
- flex 컨테이너를 선언시 아래와 같이 기본 값이 지정
  - item은 행으로 나열
  - item은 주축의 시작 선에서 시작
  - item은 교차축의 크기를 채우기 위해 늘어남
  - `flex-wrap` 속성은 `nowrap`으로 지정

```html
Tip !

justify - main axis
align - cross axis

content - 여러 줄
items - 한 줄
self - 개별 요소
```



##### flex-direction

> 쌓이는 방향 설정 (main-axis의 방향만 바뀜. flex는 single-direction layout concept이기 때문)

- row(기본값)
  - 가로로 요소가 쌓임
  - row는 주축의 방향을 왼쪽에서 오른쪽으로 흐르게 한다.
- row-reverse
- column
  - 세로로 요소가 쌓임
  - column은 주축의 방향을 위에서 아래로 흐르게 한다.
- column-reverse



##### flex-wrap

> item들이 강제로 한 줄에 배치되게 할 것인지 여부 설정



- nowrap(기본 값)
  - 모든 아이템들을 한 줄에 나타내려고 함
- wrap : 넘치면 그 다음 줄로
- wrap-reverse : 넘치면 그 윗줄로 (역순)



##### flex-flow

> flex-direction과 flex-wrap의 shorthand

```css
flex-flow: row nowrap;
```



##### justify-content

> main axis 정렬
>
> `flex-direction: row;` 기준으로 작성됨

- flex-start(기본 값)
  - 왼쪽에서 오른쪽으로 쌓임
- flex-end
  - 쌓이는 방향이 반대(`flex-direction: row-reverse;`)와는 다르다. 아이템의 순서는 그대로 정렬만 우측에 되는 것.
- center
- space-between
  - 좌우 정렬 (item들 간격 동일)
- space-around
  - 균등 좌우 정렬(내부 요소 여백은 외곽 여백의 2배)
- space-evenly
  - 균등 정렬(내부 요소 여백과 외각 여백 모두 동일)



##### align-items

> cross axis 여러 줄 정렬
>
> `flex-direction: row` 기준으로 작성됨 

- stretch(기본 값)
  - 컨테이너를 가득 채움
- flex-start
  - 위
- flex-end
  - 아래
- center
- baseline
  - item 내부의 text에 기준선을 맞춤



##### align-self

> align-items와 동일(단, 개별 item에 적용)

- auto (기본 값)
- flex-start
- flex-end
- center
- baseline
- stretch
  - 부모 컨테이너에 자동으로 맞춰서 늘어남



##### order

- 기본 값 : 0
- 작은 숫자 일수록 앞(왼쪽)으로 이동



##### flex-grow

- 기본 값 : 0
- 주축에서 남는 공간을 항목들에게 분배하는 방법
- 각 아이템의 상대적 비율을 정하는 것이 아님
- 음수는 불가능



### Bootstrap

---

##### Responsive web design

- 반응형 웹 디자인은 화면 해상도에 따라 가로폭이나 배치를 변경하여 가독성을 높인다.
- 하나의 웹사이트를 구축하여 다양한 화면 해상도에서 최적화된 웹사이트를 제공하도록 하려는 기술



### Bootstrap Grid System

---

##### Grid System

- Bootstrap의 Grid system은 containers안의 rows와 columns를 사용해서 컨텐츠를 레이웃하고 정렬한다.
  - .container > .row > .col 의 구조



##### .row

- row는 columns의 wrapper이다.
- 각 column 사이 공간을 제어하는 padding이 있는데 이를 `gutter`라 한다. row의 margin과 gutter를 제거하려면 `.no-gutters` class를 사용하면 된다.



##### .col

- column은 한 row 당 사용할 수 있는 12 col 중 사용할 col 수를 나타낼 수 있다.
- columns 너비는 백분율로 설정되기 때문에 항상 부모 요소를 기준으로 크기가 조정된다.
- grid layout에서는 반드시 columns안에 내용이 있어야 하며 columns만이 row의 하위 자식일 수 있다.



##### offset

- `offset-(number)`은 number만큼의 column 공간을 무시하고 그 다음 column부터 콘텐츠를 적용시킨다.



##### Nesting

- .row > .col > .row > .col 으로 중첩시킬 수 있다.



##### Grid Breakpoints

- Bootstrap Grid System은 다양한 디바이스에서 적용하기 위해 특정 px 조건에 대한 지점을 정해 두었는데 이를 breakpoints라고 한다.
- Bootstrap은 대부분의 크기를 정의하기 위해 em 또는 rem을 사용하지만, px는 grid breakpoint에 사용된다. (Viewport 너비가 px 단위이고 글꼴 크기에 따라 변하지 않기 때문)

