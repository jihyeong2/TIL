[TOC]

# SQL과 django ORM



##  DML,DDL, DCL, RDBMS, NOSQL

### DML

> 데이터 조작어 Data Manipulation Language

- `SELECT` : 데이터베이스에 들어 있는 데이터를 조회하거나 검색하기 위한 명령어. `RETRIEVE`라고도 함.

  ```SQL
  SELECT * FROM <table_name>;
  ```

- `INSERT` : 데이터베이스의 테이블에 데이터를 입력하기 위한 명령어

  ```sql
  -- EXAMPLE IN HOMEWORK 0922
  INSERT INTO classmates (name, age, address) VALUES('홍길동',20,'seoul');
  INSERT INTO classmates VALUES('홍길동',20,'seoul');
  INSERT INTO classmates (address,age,name) VALUES('seoul',20,'홍길동');
  ```

- `UPDATE` : 데이터베이스의 테이블에 들어있는 데이터를 수정하기 위한 명령어

  ```SQL
  UPDATE classmates SET name='홍길동', address='제주' WHERE id=4;
  ```

- `DELETE` : 데이터베이스의 테이블에 들어있는 데이터를 삭제하기 

  ```SQL
  DELETE FROM classmates WHERE id=4;
  ```



### DDL

> 데이터 정의어 Data Definition Language

- `CREATE` : 테이블과 같은 데이터 구조를 생성하기 위해 사용하는 명령어

  ```SQL
  -- EXAMPLE IN WORKSHOP 0922
  CREATE TABLE countries(
  	room_num TEXT NOT NULL,
      check_in TEXT NOT NULL,
      check_out TEXT NOT NULL,
      grade TEXT NOT NULL,
      price TEXT NOT NULL,
  )
  ```

- `ALTER` : 테이블과 같은 데이터 구조를 변경하기 위해 사용하는 명령어

  ```SQL
  ALTER TABLE classmates ADD COLUMN created_at TEXT NOT NULL DEFAULT 1;
  ```

- `DROP` : 테이블과 같은 데이터 구조를 삭제하기 위해 사용하는 명령어

  ```SQL
  DROP TABLE news;
  ```

- `RENAME` : 테이블과 같은 데이터 구조의 이름을 변경하기 위해 사용하는 명령어

  ```SQL
  ALTER TABLE classmates RENAME TO news;
  ```

- `TRUNCATE` : ??



### DCL

> 데이터 제어어 Data Control Language

- `GRANT` : ??

- `REVOKE` : ??



### RDBMS vs NOSQL

- RDBMS : 관계형 데이터베이스 관리 시스템으로 정해진 데이터 스키마에 따라 데이터베이스 테이블에 저장되며, 관계를 통한 테이블 간 연결을 통해 사용된다. 그렇기에 데이터 관리를 효율적으로 하기 위한 구조화가 중요하다.
- NOSQL : 관계형 데이터베이스와 반대되는 방식으로 스키마 개념 자체가 존재하지 않는다. 스키마가 없기 때문에 데이터를 자유롭게 관리할 수 있으며, 테이블과 비슷한 개념으로 컬렉션이라는 형태로 데이터를 관리한다.



## 기본 준비 사항

```bash
# 폴더구조

TIL
	...
	0X_db
		00_sql # only SQL
			hellodb.csv
			tutorial.sqlite3
			users.csv
		01_sql_orm # SQL + ORM
			...
			users.csv # 해당 디렉토리로 다운로드
```

* django app

  * 가상환경 세팅

  * 패키지 설치

  * migrate

    ```bash
  $ python manage.py sqlmigrate users 0001
    # 지정 마이그레이션의 SQL
    # $ python manage.py sqlmigrate <app_name> <migration_name>
    ```

* `db.sqlite3` 활용

  * `sqlite3`  실행

    ```bash
    $ ls
    db.sqlite3 manage.py ...
    $ sqlite3 db.sqlite3
    ```

  * csv 파일 data 로드

    ```sqlite
    sqlite > .tables
    auth_group                  django_admin_log
    auth_group_permissions      django_content_type
    auth_permission             django_migrations
    auth_user                   django_session
    auth_user_groups            auth_user_user_permissions  
    users_user
    sqlite > .mode csv
    sqlite > .import users.csv users_user
    -- 이미 만들어놓은 데이터 파일을 테이블에 적용하기 위한 sql문
    -- .import <file_name> <table_name>
    -- 단, 테이블에 초기 데이터가 없을 때에는 파일에 필드명을 먼저 작성해줘야 한다.
    sqlite > SELECT COUNT(*) FROM users_user;
    100
    ```

* 확인

  * sqlite3에서 스키마 확인

    ```sqlite
    sqlite > .schema users_user
    CREATE TABLE IF NOT EXISTS "users_user" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "first_name" varchar(10) NOT NULL, "last_name" varchar(10) NOT NULL, "age" integer NOT NULL, "country" varchar(10) NOT NULL, "phone" varchar(15) NOT NULL, "balance" integer NOT NULL);
    ```



---



## 문제

> 아래의 문제들을 보면서 서로 대응되는 ORM문과 SQL문을 작성하시오.
>
> **vscode 터미널을 좌/우로 나누어 진행하시오. (sqlite / shell_plus)**

`.headers on` 을 켜고 작성해주세요.



### 1. 기본 CRUD 로직

1. 모든 user 레코드 조회

   ```python
   # orm
   Users.objects.all()
   ```

      ```sql
   -- sql
   SELECT * FROM users_user
      ```

2. user 레코드 생성

   ```python
   # orm
   User.objects.create(
      ...: first_name='길동',
      ...: last_name='홍',
      ...: age=100,
      ...: country='제주도',
      ...: phone='1234',
      ...: balance=10000,
      ...: )
   ```

   ```sql
   -- sql
   INSERT INTO "users_user" ("first_name", "last_name", "age", "country", "phone", "balance")
   VALUES ('길동', '홍', 100, '제주도', '1234', 10000);
   ```

   * 하나의 레코드를 빼고 작성 후 `NOT NULL` constraint 오류를 orm과 sql에서 모두 확인 해보세요.

3. 해당 user 레코드 조회

   - `101` 번 id의 전체 레코드 조회

   ```python
   # orm
   User.objects.get(pk=101)
   ```

   ```sql
   -- sql
   SELECT * FROM users_user WHERE id=101;
   ```

4. 해당 user 레코드 수정

   - ORM: `101` 번 글의 `last_name` 을 '김' 으로 수정
   - SQL: `101` 번 글의 `first_name` 을 '철수' 로 수정

   ```python
   # orm
   user=User.objects.get(pk=101)
   user.last_lame='김'
   user.save()
   
   User.objects.get(pk=101).update(last_name='김')
   ```

      ```sql
   -- sql
   UPDATE users_user SET first_name=' 
   철수' WHERE id=101;
      ```

5. 해당 user 레코드 삭제

   - ORM: `101` 번 글 삭제
   - `SQL`:  `101` 번 글 삭제 (ORM에서 삭제가 되었기 때문에 아무런 응답이 없음)

   ```python
   # orm
   user=User.objects.get(pk=101)
user.delete()
   ```
   
   ```sql
   -- sql
   DELETE FROM users_user WHERE id=101;
   ```



---



### 2. 조건에 따른 쿼리문

1. 전체 인원 수 

   - `User` 의 전체 인원수

   ```python
   # orm
   len(User.objects.all())
   ```

   ```sql
   -- sql
   SELECT COUNT(*) FROM users_user;
   ```

2. 나이가 30인 사람의 이름

   - `ORM` : `.values` 활용
     - 예시: `User.objects.filter(조건).values(컬럼이름)`

   ```python
   # orm
   User.objects.filter(age=30).values('first_name')
   ```

      ```sql
   -- sql
   SELECT first_name FROM users_user WHERE age=30;
      ```

3. 나이가 30살 이상인 사람의 인원 수

   -  숫자/날짜/시간 필드: `__gte` , `__lte` , `__gt`, `__lt` -> 대소관계 활용
   -  문자열 필드 :
      -  `__startswith` : 조건값으로 시작하는 모든 데이터를 조회 
      -  `__endswith` : 조건값으로 끝나는 모든 데이터를 조회
      -  `__contains` : 조건값이 포함되는 모든 데이터를 조회
      -   `__istartswith` : `__startswith`와 동일하지만, 대소문자를 구분하지 않는다.
      -   `__iendswith` : `__endswith`와 동일하지만, 대소문자를 구분하지 않는다.
      -  `__icontains` : `__icontains`와 동일하지만, 대소문자를 구분하지 않는다.

   ```python
   # orm
   User.objects.filter(age__gte=30).count()
   ```

      ```sql
   -- sql
   SELECT COUNT(*) FROM users_user WHERE age>=30;
      ```

4. 나이가 20살 이하인 사람의 인원 수 

   ```python
   # orm
   User.objects.filter(age__lte=30).count()
   ```

   ```sql
   -- sql
   SELECT COUNT(*) FROM users_user WHERE age<=20;
   ```

5. 나이가 30이면서 성이 김씨인 사람의 인원 수

   ```python
   # orm
   User.objects.filter(age=30, last_name='김').count()
   ```

      ```sql
   -- sql
   SELECT COUNT(*) FROM users_user WHERE age=30 and last_name='김';
      ```

6. 나이가 30이거나 성이 김씨인 사람?

   ```python
   # orm
   User.objects.filter(Q(age=30) | Q(last_name='김')).count()
   ```

   ```sql
   -- sql
   SELECT COUNT(*) FROM users_user WHERE age=30 OR last_name='김';
   ```

7. 지역번호가 02인 사람의 인원 수

   - `ORM`: `__startswith` 

   ```python
   # orm
   User.objects.filter(phone_startswith='02-').count()
   ```

      ```sql
   -- sql
   SELECT COUNT(*) FROM users_user WHERE phone LIKE '02-%';
   -- 'A%' : 'A'로 시작하는 문자열
   -- '%A%' : 'A'를 포함하는 문자열
   -- '_A%' : 두 번째 문자가 'A'인 문자열
   -- '[ABC]%' : 첫 번째 문자가 'A' OR 'B' OR 'C'인 문자열
   -- '[A-D]%' : 첫 번째 문자가 'ABCD'에 속하는 문자열
   -- '[^A]%' : 첫 번째 문자가 'A'가 아닌 문자열
      ```

8. 거주 지역이 강원도이면서 성이 황씨인 사람의 이름

   ```python
   # orm
   User.objects.filter(country='강원도', last_name='황').values('first_name')
   ```
```sql
   -- sql
   SELECT first_name FROM users_user WHERE country='강원도' and last_name='황';
```



---



### 3. 정렬 및 LIMIT, OFFSET

1. 나이가 많은 사람순으로 10명

   ```python
   # orm
   User.objects.order_by('-age')[:10]
   ```

      ```sql
   -- sql
   SELECT * FROM users_user ORDER BY age DESC LIMIT 10;
      ```

2. 잔액이 적은 사람순으로 10명

   ```python
   # orm
   User.objects.order_by('balance')[:10]
   ```

      ```sql
   -- sql
   SELECT * FROM users_user ORDER BY balance LIMIT 10;
      ```

3. 잔고는 오름차순, 나이는 내림차순으로 10명?

      ```python
   # orm
   User.objects.order_by('balance','-age')[:10]
   ```
```sql
 -- sql
 SELECT * FROM users_user ORDER BY balance, age DESC LIMIT 10;
```

4. 성, 이름 내림차순 순으로 5번째 있는 사람

   ```python
   # orm
   User.objects.order_by('-last_name','-first_name')[4]
   ```
```sql
-- sql
SELECT * FROM users_user ORDER BY last_name DESC, first_name DESC LIMIT 1 OFFSET 4;
```



---



### 4. 표현식

> ORM: `aggregate` 사용
>
> https://docs.djangoproject.com/en/2.2/topics/db/aggregation/#aggregation
>
> - '종합', '합계' 등의 사전적 의미
> - 특정 필드 전체의 합, 평균 등을 계산할 때 사용

1. 전체 평균 나이

   ```python
   # orm
   from django.db.models import Avg
   User.objects.aggregate(Avg('age'))
   # aggregate : 모든 쿼리 셋에 적용되어 필드의 합,평균 등을 구할 때 사용하는 메서드
   # User.objects.aggregate(Sum(''))
   # annotate : 쿼리 셋의 각 객체들에 적용되어 특정 조건에 해당하는 필드들의 합, 평균 등을 구할 때 사용하는 메서드
   ```

      ```sql
   -- sql
   SELECT AVG('age') FROM users_user;
      ```

2. 김씨의 평균 나이

   ```python
   # orm
   User.objects.filter(last_name='김').aggregate(Avg('avg'))
   ```

      ```sql
   -- sql
   SELECT AVG(age) FROM users_user WHERE last_name='김';
      ```

3. 강원도에 사는 사람의 평균 계좌 잔고

   ```python
   # orm
   User.objects.filter(country='강원도').aggregate(Avg('balance'))
   ```

   ```sql
   -- sql
   SELECT AVG(balance) FROM users_user WHERE country='강원도';
   ```

4. 계좌 잔액 중 가장 높은 값

   ```python
   # orm
   from django.db.models import Max
   User.objects.aggregate(Max('balance'))
   ```

      ```sql
   -- sql
   SELECT MAX(balance) FROM users_user;
      ```

5. 계좌 잔액 총액

   ```python
   # orm
   from django.db.models import Sum
User.objects.aggregate(Sum('balance'))
   ```
   
      ```sql
   -- sql
   SELECT SUM(balance) FROM users_user;
      ```