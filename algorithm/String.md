# String

### 문자의 표현

- 미국에서 ASCII(American Standard Code for Information Interchange)라는 문자 인코딩 표준이 제정됨.
- ASCII는 7bit 인코딩으로 128문자를 표현하며 33개의 출력 불가능한 제어 문자들과 95개의 출력 가능한 문자들로 이루어짐.

- Byte :  영문자 한자를 나타내는 단위(8bit)
- Bit : 정보를 나타내는 최소 단위
- 유니코드 인코딩(UTF : )



### 문자열

- 문자열은 시퀀스 자료형으로 분류된다. -> index로 접근이 가능하고, Slicing 사용 가능
- 문자열 클래스에서 제공되는 메소드
  - replace(), split(), isalpha(), find()
- 문자열은 튜플과 같이 요소 값을 변경할 수 없다.(immutable)

- C와 Java의 String 기본적인 차이점
  - C는 아스키 코드로 저장
  - Java는 유니코드(UTF16, 2byte)로 저장
  - 파이썬은 유니코드(UTF8)로 저장