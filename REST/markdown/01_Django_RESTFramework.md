# Django REST Framework

> 2020.10.05



## 1. API

> 프로그래밍을 통해 제어??



### 1.1 API Server

> 프로그래밍을 통해 요청에 JSON을 응답하는 서버를 만들기



### 1.2 RESTFUL API

> 엄격한 의미로 REST는 네트워크 아키텍처 원리의 모음이다. 여기서 '네트워크 아키텍처 원리'란 자원을 정의하고 자원에 대한 주소를 지정하는 방법 전반을 일컫는다. 간단한 의미로는, 웹 상의 자료를 HTTP위에서 전송하기 위한 아주 간단한 인터페이스를 말한다.

- 자원(URI) 
  - URL(Uniform Resource Locator) 파일 식별자
  - URI(Uniform Resource Identifier) 통합 자원 식별자 : 하나의 리소스를 가리키는 문자열이다. 가장 흔한 URI는 URL로, 웹 상에서의 위치로 리소스를 식별한다.
- 행위(HTTP Method)
  - HTTP(Hyper Text Transfer Protocol) : 컨텐츠를 전송하기 위한 프로토콜(규약)
  - Stateless : 상태 정보가 저장되지 않음
  - Connectless : 서버에 요청을 하고 응답을 한 이후에 연결은 끊어짐
  - GET : 지정 리소스의 표시를 요청하며, 오직 데이터를 받기만 함.
  - POST :  클라이언트 데이터를 서버로 보냄
  - PUT/PATCH : 서버를 보낸 데이터를 저장/지정 리소스의 부분만을 수정
  - DELETE : 지정 리소스를 삭제
- 표현(Representations)

- JSON(JavaScript Object Notation) : 자바스크립트 객체 표기법, 쉽게 말해 데이터 덩어리이다.



## 2. DRF



### 2.1 DRF vs Django

|          |  Django   |       DRF       |
| :------: | :-------: | :-------------: |
| Response |   HTML    |      JSON       |
|  Model   | ModelForm | ModelSerializer |











