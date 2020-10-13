# HTML

> 웹 컨텐츠의 의미와 구조를 정의할 때 사용하는 언어

## HTML 기초

#### Hyper

- 텍스트 등의 정보가 동일 선상에 있는 것이 아닌 다중으로 연결된 상태



#### Hyper Text

- 참조(하이퍼링크)를 통해 다른 문서로 접근할 수 있는 텍스트
- 하이퍼 텍스트가 쓰인 기술들 중 가장 중요한 두 가지 (HTTP, HTML)



#### Markup Language

- "마크업을 한다."는 말은 특정 텍스트에 역할을 부여한다는 말이다.
- `<h1>`Tag는 단순 크기만 커지는 것이 아닌, 그 페이지에서 가장 핵심 주제를 의미하는 것이다.



## HTML 기본 구조

#### DOM

- DOM은 문서의 구조화된 표현을 제공하며 프로그래밍 언어가 DOM 구조에 접근할 수 있는 방법을 제공하여 문서 구조와 내용 등을 변경할 수 있게 도움.
- 웹 페이지의 객체 지향 표현



#### Element

- HTML 요소는 시작 태그와 종료 태그, 그 사이에 포함된 내용으로 구성된다.
- 내용이 없는 태그들
  - `<br>`,`<hr>`,`<img>`,`<input>`,`<link>`,`<meta>`
- 각 요소들은 중첩될 수 있다. (단, 태그 쌍이 맞는지 잘 확인해야 함.)



#### Attribute

- Attribute는 태그 안에 부가적인 정보를 담고 있다.
- 요소의 시작 태그에 위치해야 하며 파일 경로, 크기, Class, id 등 추가정보를 담고, 이름과 값의 쌍을 이루고 있다.



#### Sementic Tag

> 브라우저, 검색엔진, 개발자에게 콘텐츠의 의미를 명확히 설명하는 태그



**장점**

1. 읽기 쉬어진다. (개발자)
   - 요소의 의미가 명확히 드러나고 코드의 가독성을 높이며, 유지보수를 쉽게 한다.
2. 접근성이 좋아진다. (검색엔진 및 보조기술 -> 시력장애용 스크린 리더 -> 더 나은 경험 제공)
   - HTML 문서는 HTML 언어 + 사람이 읽을 수 있는 content의 조합인데, 검색엔진은 HTML 코드만 잘 읽는다.
   - 그렇기 때문에 검색 엔진이 HTML을 잘 이해하도록 시맨틱 태그 사용을 권장한다.

##### Sementic Web

- 웹에 존재하는 수많은 웹페이지들에 메타데이터를 부여하여, 기존의 단순한 데이터 집합이었던 웹페이지를 의미와 관련성을 가지는 거대한 데이터베이스로 구축하고자 하는 발상.