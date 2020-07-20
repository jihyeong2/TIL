# Git 정리

> Git은 분산버전관리시스템이다.

## 준비하기

> 윈도우에서 Git을 활용하기 위해서 [Git Bash](https://git-scm.com/)를 설치합니다. 

> 초기 설치를 완료한 이후에, 계정 설정을 진행합니다.

```sh
$ git config --global user.email {이메일 주소}
$ git config --global user.name {유저네임}
```

## 로컬 저장소 활용하기

### 1. 저장소 초기화

> 이제부터 이 디렉토리를 Git으로 관리하겠다(변경 이력을 감시하겠다)

```sh
$ git init
```

- `.git`디렉토리가 생성되며, 여기에 Git과 관련된 모든 정보가 저장됩니다.
- 초기화를 하고 나면 Git Bash에 `(master)` 라고 표시가 되는데, 이는 이 디렉토리는 이미 Git이 관리하고 있다는 뜻으로 생각할 수 있습니다.
- 이미 초기화한 repo에서는 다시 git init을 하지 않습니다. (중요!)

### 2. add

> working directory 작업공간에서 변경된 사항을 이력으로 관리하기 위해서는 반드시 staging area를 거쳐야 한다.

```sh
$ git add {staging 할 파일}
```

### 3. Commit

> 이력을 확정짓는 명령어이다. (기록을 확정짓는 명령어)

```sh
$ git commit -m '커밋 메세지'
```

> 커밋 기록을 확인하고 싶다면 아래의 명령어를 참고하세요.

```sh
$ git log
```

### 4. Status

> git을 쓰면서 가장 많이 사용해야 하는 명령어이며, 현재 상황을 확인하는 명령어이다.

```sh
$ git status
```

## 원격 저장소 활용하기

> 여러 서비스 중, github를 기준으로 설명합니다. 

### 1. 준비사항

- github에 가입 후, 빈 repo를 만들어둔다.

### 2.원격 저장소 등록

- 로컬 저장소와 원격 저장소를 연결하는 일입니다.

```sh
$ git remote add origin {github repo url}
```

- 원격 저장소(remote)를 등록할건데, `origin`이라는 이름으로 원격 저장소를 등록하겠다. 
- 원격 저장소 등록 현황을 확인하려면 아래의 명령어를 참고하세요.

```sh
$ git remote -v
```

