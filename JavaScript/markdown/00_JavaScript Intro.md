[TOC]

# JavaScript Intro

> 2020.10.20



## 1. JavaScript



### 1.1 DOM(Document Object Model) Manipulate

- 웹 브라우저가 HTML 페이지를 인식하는 방식으로 Document 객체와 관련된 객체의 집합이다. Document와 관련된 객체를 생성하여 조작할 수 있다.

- 모든 문서의 노드는 `DOM Tree`라고 불리우는 트리 구조이다.



### 1.2 BOM(Browser Object Model) Manipulate

- 웹 브러우저와 관련된 객체의 집합으로 대표적으로는 window, location, navigator 등의 객체가 있다. 브라우저와 관련된 객체를 생성하여 조작할 수 있다.



### 1.3 ECMA(European Computer Manufacturer's Association) Script

- ECMAScript는 JavaScript와 같은 스크립트 언어의 표준을 말한다. JavaScript는 ECMAScript를 기반으로 만들어졌으며, ECMAScript 언어 중 가장 인기 있는 언어이다.



## 2. CRUD by JavaScript

### 2.1 Create

- `createElement` : 조건에 맞는 태그를 생성하는 메서드이다. 

- `append / appendChild` : `append`와 `appendChild` 메서드를 활용하여 생성한 태그를 document에 삽입한다.

  | append                                                       | appendChild                                             |
  | ------------------------------------------------------------ | ------------------------------------------------------- |
  | 마지막 자식 뒤에 `Node` 객체 또는 `DOMString` 객체를 삽입한다. | `DOMString` 객체가 아닌 `Node` 객체만을 삽입할 수 있다. |
  | 반환하는 값이 없다.                                          | `Node.appendChild()`는 추가한 `Node` 객체를 반환한다.   |
  | 여러 개의 노드와 문자를 추가할 수 있다.                      | 오직 하나의 노드만을 추가할 수 있다.                    |

  

### 2.2 Read

- `querySelector` : id, class, tag, 복합 선택자(자손, 자식 선택자) 등 다양한 조건을 활용하여, 해당 조건에 만족하는 하나의 객체만을 선택한다.

- `querySelectorAll` : `querySelector` 와 같이 다양한 조건을 활용할 수 있지만, 이는 해당 조건에 만족하는 모든 객체들을 선택한다.

- `getElementById` : id가 일치하는 객체를 선택할 수 있다. 하지만, `querySelector`와 다르게 id만을 조건으로 활용할 수 있어 많은 제약이 따른다. `getElementByTagName`, `getElementByClassName` 도 있지만, 하나의 조건만을 활용할 수 있다.

```javascript
const header = document.querySelector('h1')

const frameworkLi = document.querySelectorAll('.framework')

const selectOne = document.querySelector('.lang')

const selectDescendant = document.querySelector('body li')

const selectChild = document.querySelector('body > li')

const headerAttr = header.getAttribute('id')
// getAttribute(String name)
// 이름이 name인 속성의 값들을 구한다.
// 지정한 이름의 속성이 존재하지 않을 경우 null을 반환한다.

const headerAttrName = header.getAttributeNames()
// getAttributeNames()
// 속성의 이름 목록을 구한다.
```



### 2.3 Update

- 선택한 element의 text, style 등등 원하는 속성을 변경할 수 있다.

```javascript
header.innerText='Browsers'

h1.style.color = 'blue'

h1.setAttribute('id', 'header')
// setAttribute(String name, Object value)
// 이름이 name인 속성의 값을 value로 지정한다.
```



### 2.4 Delete

- `remove / removeChild` : `remove`와 `removeChild`를 사용하여 Element를 삭제할 수 있다.

  | remove                      | removeChild                                                  |
  | --------------------------- | ------------------------------------------------------------ |
  | 부모 요소가 필요없다.       | 부모요소가 필요하다.                                         |
  | 반환 값이 없다.             | 삭제한 노드의 주소를 반환한다.                               |
  | 노드를 메모리에서 삭제한다. | 메모리에서 노드를 삭제하지 않고 부모-자식 관계를 끊어 DOM 트리에서 해제시킨다. |

- `removeAttribute` : 이름이 메서드의 인자인 속성을 삭제한다.