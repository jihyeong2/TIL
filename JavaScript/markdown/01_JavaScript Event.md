[TOC]

# JavaScript Event

2020.10.20



## 1. Event

> `HTML` 문서 내에서 일어나는 사건 (`click`, `submit`, `keydown`...)



### 1.1 addEventListner



```javascript
EventTarget.addEventListener(type, listener)
```

- `EventTarget` : 이벤트 감지를 위한 요소

- `addEventListener` : `EventTarget`에 이벤트를 등록할 때 사용하는 이벤트 핸들러
- `type` : 이벤트의 종류 (`click`, `submit`, `keydown`...)
- `listener` : `CallbackFunction` 으로 이벤트가 발생하면 실행되는 함수



### 1.2 event.preventDefault

- 각 태그의 기본으로 설정된 이벤트가 브라우저에서 동작하지 않도록 막는 행위

