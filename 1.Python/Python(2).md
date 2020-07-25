# Data Container

> Container란 여러 개의 값을 저장할 수 있는 것(객체)



### 1. Sequence Container

> 데이터가 순서대로 나열된 형식을 나타낸다.



- List
  - List는 `[]` , `list()` 를 사용하여 만들 수 있다.
  - List[index]를 통해 특정 위치의 값에 접근할 수 있다.
- Tuple
  - Tuple은 `()` 를 사용하여 만들 수 있다.
  - List와 달리 수정이 불가능하며, 읽는 용도로 밖에 사용할 수 없다.
- Range
  - range(n) : 0~n-1까지 순서대로 값을 가짐.
  - range(n,m) : n~m-1까지 순서대로 값을 가짐.
  - range(n,m,s) : n~m-1까지 s씩 증가하는 값을 가짐.

- Operator & Function in Sequence Container

| operation  | 설명                                       |
| ---------- | ------------------------------------------ |
| x in s     | If 'x' is in 's', return true              |
| x not in s | If 'x' is not in 's', return true          |
| s1 + s2    | It connect s1 to s2                        |
| s * n      | It repeatly connect s to s for n times     |
| s[i]       | It is i-th data in s                       |
| s[i:j]     | It is from i-th data to (j-1)-th data in s |
| len(s)     | It is length of s                          |
| min(s)     | It is minimum value of s                   |
| max(s)     | It is maximum value of s                   |
| s.count(x) | It is the number of data in s              |



### 2. Non-Sequence Container

- Set
  - Set is Non-Sequence Data Constructure.
  - It is same set in math.
  - It is created of `{}`  and `set()` .
  - The data in set is not overlapped.

```python
s = set()
s = {}
```



- Dictionary
  - It is created of `{}` and `set()`.
  - It is made of `key` and `value` . `Key` is only possible immutable data(String, Integer, Float, Boolean, Tuple, Range).
  - `Value` is possible all data of type included `list` ,`dictionary`.



### 3. Typecasting

- The container can convert to each other.



