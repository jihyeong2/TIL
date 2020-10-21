[TOC]

# AJAX

> 2020.10.20



## 1. AJAX(Asynchronous Javascript And XML)

> 서버와 통신하기 위해  XMLHttpRequest 객체를 사용하는 것

- 페이지를 reload하지 않고 요청 작업을 비동지적으로 수행할 수 있다. (사용자 경험 향상)
- 페이지의 전체가 아닌 일부만을 업데이트 할 수 있다.
- HTML, JSON, XML, 일반 텍스트를 교환할 수 있다.

- `XHR(XMLHttpRequest) `
  - 서버와 상호작용하기 위해 사용한다. 전체 페이지의 새로고침 없이 데이터를 받아올 수 있다.
  - 사용자가 하는 것을 방해하지 않고 페이지의 일부를 업데이트 할 수 있다.
  - 주로 AJAX 프로그래밍에 사용한다.



### 1.1 Asynchronous

> "기다려주지 않는다."!



```python
import requests
import json


res = requests.get('https://jsonplaceholder.typicode.com/todos/1').text

print(res) # { 'userId': 1, 'id': 1, 'title': 'delectus aut autem', ... }
```

```javascript
const xhr = new XMLHttpRequest()

xhr.open('GET', 'https://jsonplaceholder.typicode.com/todos/1')
xhr.send()

const res = xhr.response

console.log(res) // ''
```

- 아래 코드에서는 json 파일의 정보가 출력되지 않는다. 



### 1.2 Single Thread

> "혼자 일하기 때문에 기다릴 수가 없다."

- 외부 서버로 요청을 보내는 상황
  - 요청을 보낸다.
  - 다음 할 일들을 한다.
  - 응답이 오면 그 때 그 일을 처리한다.

**JavaScript는 외부로 요청할 일이 있으면 요청만 보내고 끝이다. 요청을 보내면 Web api에서 요청한 일을 수행하고, JavaScript는 다음 명령들을 실행한다. **



### 1.3 Event Loop

>  "JavaScript가 혼자서 일하는 방법"

- Call Stack
  - 함수의 호출을 기록하는 Stack 자료구조이다.
  - 한 번에 하나의 작업만을 처리할 수 있으며, 함수의 처리는 Stack이 다시 비워질 때까지 계속 이어진다.
- Web API(Browser API)
  - 브라우저에서 제공하는 API이다.
  - `setTimeout`, `setInterval`, `XHR`
- TaskQueue
  - Callback Function이 대기하는 Queue 자료구조이다.
  - 전송 순서대로 작업을 처리하기 위해 Queue 자료구조를 사용한다.
- Event Loop
  - Call Stack이 비어있으면 Task Queue의 함수를 Call Stack으로 보낸다.
- Callback Function
  - 다른 함수의 인자로 전달되는 함수이며, 1급 객체라고 한다. (return 값, 함수 인자, 변수로 사용 가능하면 1급 객체라고 한다.)



**비동기 처리 과정은 요청한 결과가 처리되는 '특정 시점'에 'CallBackFunction'을 실행하는 형태로 이루어진다. 비동기 처리에 CallbackFunction은 반드시 필요하지만, 그렇다고 해서 CallbackFunction을 사용하는 모든 로직이 비동기는 아니다. CallbackFunction이 연달아 수행되도록 할 수도 있지만, 여러 번 반복되면 CallbackHell로 이어질 수 있어 주의해야 한다.**



### 1.4 Promise

- 비동기 작업이 실행됐을 때, 성공과 실패를 약속하는 객체

  - CallbackHell을 해결하기 위해 ES6(ECMAScript)부터 등장한 개념이다.
  - `.then(Callback Function)` : 요청이 성공적으로 이루어지면 어떻게 처리할지에 대한 내용이 들어간다.
  - `.catch(Callback Function)` : 요청이 실패하면 어떻게 처리할지에 대한 내용이 들어간다.

- `Axios` : Promise 기반의 비동기 요청을 할 수 있는 JavaScript 라이브러리

  ```javascript
  axios.get('https://jsonplaceholder.typicode.com/todos/asdf')
  	// Promise의 성공/실패에 대한 약속 이후의 처리를 할 수 있다.
    .then(function (res) {
      console.log(res)
      return res.data
    })
  	// 이전 .then 내부 CB의 return 값은 다음 .then 내부 CB의 인자로 넘어온다.
    .then(function (data) {
      console.log(data)
      return data.title
    })
    .then(function (title) {
      console.log(title)
    })
  	// Error는 요청를 1이 아닌 asdf로 변경해서 확인해보자
    .catch(function (err) {
      console.log(err)
    })
  // Axios도 내부적으로 XMLHttpRequest를 사용한다.
  ```

  

- `async & await` : 비동기 방식으로 처리하는 로직을 마치 동기적으로 보이게 만드는 방식

  - function 앞에 `async` 키워드를 작성하고 함수 내에서 비동기적으로 처리되는 로직앞에 `await` 키워드를 작성한다.
  - `await` 연산자는 `Promise`를 기다리기 위해 사용하는데, `async function` 내부에서만 사용해야 원하는 방식으로 동작한다.

  ```javascript
  // 함수 앞에 async 키워드를 작성한다.
  async function getTodo () {
    console.log('1')
    // Promise를 return하는 로직 앞에 await 키워드를 작성한다.
    await axios.get('https://jsonplaceholder.typicode.com/todos/1')
      .then(function (res) {
        console.log(res)
       })
    console.log('2')
  }
  
  getTodo()
  ```

  