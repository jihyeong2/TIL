## Make Python a Python

> 2020.10.12



### 몫과 나머지 - divmod

```python
a=5
b=3
print(*divmod(a,b))
```



### n진법으로 표기된 string 10진법 숫자로 변환하기 - int함수

```python
num='11123'
base=5
answer=int(num,base)
```



### 문자열 정렬하기 - ljust, center, rjust

```python
s = '가나다라'
n = 7

s.ljust(n) # 좌측 정렬
s.center(n) # 가운데 정렬
s.rjust(n) # 우측 정렬
```



### 알파벳 출력하기 - string 모듈

```python
import string
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.ascii_letters)
string.digits
```



### 2차원 리스트 뒤집기 - zip

```python
# python의 zip과 unpacking을 이용하면 쉽게 리스트를 뒤집을 수 있다.
my_list=[[1,2,3],[4,5,6],[7,8,9]]
new_list=list(map(list,zip(*my_list)))

# zip은 각 iterables의 요소들을 모으는 이터레이터를 만든다.
# 튜플의 이터레이터를 돌려주는데, i 번째 튜플은 각 인자로 전달된 시퀀스나 이터러블의 i 번째 요소를 포함한다.
```



### 모든 멤버의 type 변환하기 - map

```python
list1 = ['1','103','3424']
list2 = list(map(int, list1))
# iterable의 모든 멤버의 type을 map함수를 통해 변환할 수 있다.
```



### sequence 멤버를 하나로 이어붙이기 - join

```python
my_list = ['1','103','3424']
answer = ''.join(my_list) # -> '11033424'
```



### 삼각형 별찍기 - sequence type의 * 연산

```python
n = 3
for i in range(1,n+1):
    print('*'*i)
# * 연산자를 사용해 문자열을 원하는 갯수만큼 늘릴 수 있다.
```



### 곱집합 구하기 - product

```python
import itertools
s1='ABCD'
s2='xy'
s3='1234'
itertools.product(s1,s2,s3)
```



### 2차원 리스트를 1차원 리스트로 만들기 - from_iterable

```python
my_list=[[1,2],[3,4],[5,6]]
# 1.
answer=sum(my_list,[])
# 2.
import itertools
list(itertools.chain.from_iterable(my_list))
# 3.
import itertools
list(itertools.chain(*my_list))
# 4.
[element for array in my_list for element in array]
# 5.
from functools import reduce
list(reduce(lambda x, y: x+y, my_list))
# 6.
from functools import reduce
import operator
list(reduce(operator.add, my_list))
# 7.
import numpy as np
np.array(my_list).flatten().tolist()
```



### 순열 조합 - from itertools

```python
from itertools import permutations
def solution(mylist):
    mylist.sort()
    answer = list(map(list,permutations(mylist)))
    return answer
# 조합은 combinations
print(solution([2,1]))
```



### 가장 많이 등장하는 알파벳 찾기

```python
import collections
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 7, 9, 1, 2, 3, 3, 5, 2, 6, 8, 9, 0, 1, 1, 4, 7, 0]
answer = collections.Counter(my_list)
print(answer[1]) # = 4
print(answer[3])  # = 3
print(answer[100]) # = 0
```



### for문과 if문을 한번에 - List comprehension의 if문

```python
my_list=[3,2,6,7]
answer=[i**2 for i in my_list if i%2==0]
```



### flag OR else

```python
import math

numbers = [int(input()) for _ in range(5)]
multiplied = 1
for number in numbers:
    multiplied *= number
    if math.sqrt(multiplied) == int(math.sqrt(multiplied)):
        print('found')
        break
else:
    print('not found')
```



### 이진탐색 알고리즘

```python
import bisect
mylist=[1,2,3,7,8,9,11,33]
print(bisect.bisect(mylist,3))
# 리스트가 정렬되어 있다는 가정 하에 x값이 들어갈 위치를 반환한다.
# 경계값은 오른쪽으로 포함시킨다.
# bisect_left는 경계값을 왼쪽으로 포함시키는 알고리즘이지만, bisect(bisect_right)를 더 많이 사용한다.
```



### 클래스 인스턴스 출력하기 - class의 자동 string casting

```python
class Coord(object):
    def __init__ (self, x, y):
        self.x, self.y = x, y
    def __str__ (self):
        return '({}, {})'.format(self.x, self.y)

point = Coord(1, 2)
# __str_ 메서드를 사용해 class 내부에서 출력 format을 설정할 수 있다.
```



### 가장 큰 수, inf

```python
min_val = float('inf')
print(99999999999999999>min_val) # -> 무조건 False
max_val = float('-inf')
print(-9999999999999999999999999999>max_val) # -> 무조건 True
```



### 파일 입출력 간단하게 하기

```python
with open('myfile.txt') as file:
  for line in file.readlines():
    print(line.strip().split('\t'))
# with-as 구문을 사용하면 파일을 close하지 않아도 되며, 블록이 종료되면 파일도 자동으로 종료된다.
# readlines가 EOF까지만 읽으므로, while문 안에서 EOF를 체크할 필요가 없다.
```

