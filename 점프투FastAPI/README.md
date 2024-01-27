<img width="365" alt="image" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/f1797620-132b-44c3-9cf1-d782da142f50"><img width="209" alt="image" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/a8c49153-3a2d-4e23-9dd3-b0045a27cb9b"><img width="682" alt="image" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/a3f12bb0-b5de-4a53-a507-0642378f042b"># 1장. FastAPI 개발준비!

## 1. 파이썬 가상 환경 사용
<img width="450" alt="image" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/77d5d843-7513-4c96-873b-7399ab6b3512">
<img width="450" alt="image" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/140ca6e9-4a65-4e15-ac49-2c6fb3e6fbba">

```shell
python -m venv myapi  # myapi라는 이름의 가상 환경을 생성
.\myapi\Scripts\activate  # 가상 환경에 진입하기
    (myapi) ~ # 가상 환경으로 진입한 상황
deactivate    # 가상 환경 벗어나기
```
- 파이썬 가상 환경은 프로젝트를 진행할 때 독립된 환경을 만들어준다
- 파이썬 가상 환경을 이용하면 하나의 PC 안에 독립된 가상 환경을 여러개 만들어서 서로 다른 버전에 대해서도 관리할 수 있다
- vscode에서 할 때, powershell이 아니라 command prompt에서 명령어를 입력해야 한다

<br>

```shell
pip install fastapi                    # 가상 환경에 fastapi 설치
python -m pip install --upgrade pip    # 가상 환경의 pip 최신 버전으로 설치
```

## 2. Svelte 개발 환경 준비하기
- Svelte : React, Vue.js 등과 비슷한 역할을 하는 프론트엔드용 웹 프레임워크
- Svelte의 장점
  1. Write less code : 다른 프론트엔드 프레임워크에 비하여 작성해야 할 코드가 적다
  2. No virtual Dom : React나 Vue.js와 같은 프레임워크는 가상돔을 사용하지만 Svelte는 가상돔을 사용하지 않고 실제 Dom을 반영
  3. Truely reactive : 복잡한 상태 관리를 위한 지식 및 라이브러리들이 필요 없다

### Node.js 설치
<img width="450" alt="image" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/05e1ad20-de10-4f27-bb02-03df638516d3">
<img width="450" alt="image" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/35b7acad-b7bd-4f6a-817f-a05856507dad">

- 위와 같이 출력되면 Node.js가 깔리지 않은 상황이다
- 이러한 경우 https://nodejs.org에 접속하여 최신 버전 말고 recommended 버전으로 node.js를 다운로드 한다

<img width="900" alt="image" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/77d7abc6-6e99-4692-8d77-6ac15d7a1adc">

```
npm create vite@latest frontend -- --template svelte # Vite와 Svelte를 사용하여 새로운 프로젝트를 생성하는 npm 명령어
cd frontend  
npm install  # Svelte 애플리케이션을 설치
```

- command prompt에서 위의 명령어를 실행하여 svelte를 가상 환경에 설치한다
- 추가적으로 VSCode에서 "Svelte for VSCode"라는 Extension을 설치해줘야 한다

<br>

### JavaScript TypeCheck 설정 끄기
<img width="635" alt="image" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/bd985b0f-4440-4770-b3f2-6b43cb1d6e14">

- Svelte(스벨트)는 자바스크립트의 타입을 체크하는 것이 default로 설정되어 있다
- 하지만 파이보 프로젝트는 Typescript를 사용하지 않기 때문에 해당 설정을 끄고 진행하도록 한다
- 이를 위해 frontend/jsconfig.json 파일을 열고 "checkJs" 부분을 false로 수정한다

<br>

### Svelte 서버 실행하기

<img width="450" alt="image" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/c5ebe5d2-fe7e-4754-b988-9dff0ce540de">
<img width="450" alt="image" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/2b02c251-7086-4e7d-a817-f4bf02157c08">

- "npm run dev" 명령어를 실행하여 npm 스크립트 중 "dev" 스크립트를 실행한다
- 이를 통해 개발 서버 실행, Hot Module Replacement, 라이브 리로딩이 가능해진다
- 주어진 로컬 IP로 접속하면 Svelte 서버에 접속하게 된다
    - cf) 프론트엔드 서버가 필요한 이유
      - Svelte로 작성한 코드를 실시간으로 테스트하려면 Svelte로 작성한 코드를 브라우저가 인식할 수 있는 HTML, CSS, Javascript로 실시간 변환하는 기능이 필요하다
      - 이러한 실시간 변환을 위해 Node.js 서버가 필요하다
      - 물론 Svelte로 작성한 코드를 빌드하고 HTML, CSS, Javascript를 FastAPI 서버에 정적 파일 형태로 배포하면 된다
      - 즉, 운영 단계에서는 Node.js 서버가 필요 없다

<br>

## 3. Hello API 만들고 테스트하기
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def hello():
    return {"message" : "안녕하세요 파이보"}
```
```
pip install "uvicorn[standard]"  # uvicorn 설치
uvicorn main:app --reload        # FastAPI 서버 구동
```

<img width="564" alt="image" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/05bf274a-4473-4d14-b39e-4329c3eaa60e">

- main.py 파일을 myapi(가상 환경)에 생성한다
- 비동기 호출을 지원하는 파이썬용 웹 서버인 uvicorn을 설치하고 이를 통해 FastAPI 서버를 구동한다
- main:app에서 main은 main.py 파일을 의미하고 app은 main.py의 fastapi 객체인 'app'을 의미한다
- --reload 옵션은 프로그램이 변경되면 서버 재시작 없이 그 내용을 반영하는 것이다

<br>

## 4. Svelte 웹 페이지 만들기
<img width="450" alt="image" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/f9610b26-1b48-4c36-8354-8cf8b19a8f5f">
<img width="450" alt="image" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/ca6514b3-5a67-404f-b057-a0a021aac7a2">

- 백엔드의 Hello API를 완성하였으니 프론트 엔드 영역에서 웹 페이지를 만들 차례이다
- myapi/frontend/src/App.svelte를 수정하여 문구를 수정할 수 있고, myapi/frontend/src/app.css를 수정하여 문구의 스타일을 수정할 수 있다
- 우선 App.svelte를 수정해서 <script> 블록에서 message라는 변수를 생성하고 FastAPI의 hello API를 호출하여 돌려받은 값을 message 변수에 담고 출력하게 한다
- 그러나 undefined로 나오는데 이는 CORS 정책에 의해 요청이 거부되었기 때문이다(= 프론트엔드에서 FastAPI 백엔드 서버로 호출이 불가능한 상황)
- 이를 해결하기 위해 FastAPI에 CORS 예외 URL을 등록하여 해결할 수 있

<br>

<img width="458" alt="image" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/fb1325e4-8d00-4970-a0c0-b25b56d77917">

```python
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    'http://127.0.0.1:5173',
    'http://localhost:5173',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
) 
```
- main.py에 위의 코드를 추가하여 문제를 일으켰던 Svelte 서버의 주소를 CORS 예외 주소로 등록하고 오류를 해결할 수 있다
- 이렇게 main.py에서 설정한 GET Method의 반환값을 Svelte로 구성한 프론트 엔드 웹에서 출력하는 것을 실습했다

<br>

# 2장. 개발 기초 공사

## 1. FastAPI 프로젝트의 구조
```
|___ main.py            # FastAPI 프로젝트의 전체적인 환경을 설정하는 파일
|___ database.py        # 데이터베이스와 관련된 설정을 하는 파일
|___ models.py          # 모델 클래스들을 정의하는 파일
|___ domain             # 프로젝트가 목표하는 게시판에 필요한 3가지 도메인(질문, 답변, 사용자) 
|    |___ answer            # 각 도메인은 API를 생성하기 위해 다음 파일들이 필요하다
|    |___ question          # 라우터 파일 : URL과 API의 전체적인 동작을 관리
|    |___ user              # 데이터 베이스 처리 파일 : CRUD를 처리
|                           # 입출력 관리 파일 : 입력 데이터와 출력 데이터의 스펙 정의 및 검증
|___ frontend           # Svelte 프레임워크를 설치한 디렉토리, 하위에 dist 디렉토리에 생성된 빌드 파일로 배포 예정
```

## 2. 모델로 데이터베이스 관리하기

<img width="446" alt="image" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/02f6f327-0f62-4f19-80e7-5d5f5f822af5">

- 데이터베이스를 사용하려면 SQL 쿼리라는 구조화된 질의를 작성하고 실행하는 등의 과정이 필요하다
- 이 때 ORM(object relational mapping)을 이용하면 파이썬 문법으로도 데이터 베이스를 다룰 수 있다
- 즉, ORM을 이용하면 개발자가 Query를 직접 작성하지 않아도 데이터베이스의 데이터를 처리할 수 있는 것이다

<br>

```
pip install sqlalchemy     # SQLAlchemy(ORM) 라이브러리 설치
pip show sqlalchemy        # SQLAlchemy가 제대로 설치되었는지 확인
# database.py 생성
# models.py 생성

pip install alembic        # models.py에 작성한 모델을 이용하여 테이블을 생성하고 변경할 수 있게 하는 라이브러리 설치
alembic init migrations    # alembic 초기화 작업 수행
# ./alembic.ini 수정
# ./migrations/env.py 수정
alembic revision --autogenerate    # 리비전 파일 생성
alembic upgrade head               # 리비전 파일 실
```

### 모델을 이용해 테이블 자동으로 생성하기

<img width="450" alt="image" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/93636a9b-e9a6-4bb0-b349-402c26ad5639">
<img width="450" alt="image" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/c705d553-ed2a-4b3d-8779-29fbf283dbf2">

- alembic init migrations로 생성된, myapi 하위의 alembic.ini과 migrations 하위의 env.py를 위와 같이 수정한다
- alembic.ini에는 sqlalchemy.url을 연결한 DB 주소로 변경하고, env.py에는 models.py에서 설정한 Base 클래스를 넣어준다

<br>

<img width="773" alt="image" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/e64dd22a-9760-41b8-b9f9-d0a4b938191e">

- alembic revision --autogenerate 를 통해 migrations/versions 하위에 리비전 파일을 생성한다
- 리비전 파일은 py 확장자를 가지고 있는 파일로 무작위적으로 만들어지며, 테이블 생성 또는 변경하는 실행문들이 들어있다
- 해당 명령어는 myapi(alembic init이 있는 가상 환경 메인 디렉토리)에서 실행해야 한다

<br>

<img width="468" alt="image" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/b474bd25-cb90-47a6-933b-8190f5573a59">

- alembic upgrade head로 리비전 파일을 실행하여 데이터 베이스 모델에 정의한 question과 answer라는 이름의 테이블을 생성한다
- myapi/myapi.db라는 SQLite 데이터베이스 데이터 파일 형태로 생성되었을 것이다
- 이를 살펴보기 위해 SQLite GUI 도구인 DB Browser for SQLite를 사용해야 한다

<br>

<img width="600" alt="image" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/16e974cf-8a9e-4f01-ba84-11434e3cd5e7">
<img width="300" alt="image" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/b614d3f3-537d-4d9e-b3ae-ed9f856b0028">

- https://sqlitebrowser.org/dl 에 접속하여 운영체제에 맞는 설치 파일을 내려받고 설치 중 shortcuts 옵션을 추가한다

<br>

<img width="700" alt="image" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/2070f76c-84ac-4348-b3b5-ea0e0ecb70aa">
<img width="700" alt="image" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/a6f89197-88ca-4927-86f6-52998db2fc97">

- 설치된 DB Browser for SQLite를 이용하여 myapi.db 파일을 열면 위와 같이 answer, question 테이블이 생성된 것을 확인할 수 있다
- VSCode에서 "SQLite Viewer" Extension을 다운로드 하면 두 번째 사진과 같이 VSCode에서 myapi.db를 볼 수 있다

<br>

## 3. 모델로 데이터 처리하기

### 질문 저장하기

<img width="686" alt="image" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/5d591561-298d-426c-b162-5c898ea797d8">

```
from models import Question, Answer
from datetime import datetime
q = Question(subject='pybo가 무엇인가요?', content='pybo에 대해서 알고 싶습니다.', create_date=datetime.now())

from database import SessionLocal
db = SessionLocal()
db.add(q)
db.commit()
q.id        # 출력 결과 : 1

q = Question(subject='FastAPI 모델 질문입니다.', content='id는 자동으로 생성되나요?', create_date=datetime.now())
db.add(q)
db.commit()
q.id        # 출력 결과 : 2
```

- commit : commit은 변경 사항을 db에 적용하는 것으로 일종의 결정 사인이고 그렇기 때문에 수행한 작업을 취소할 수 없다는 점을 유의해야 한다
- rollback : 수행한 작업을 취소하는 역할로 commit 이전에 진행해야 한다

<br>

### 데이터 조회, 수정, 삭제

<img width="534" alt="image" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/f4072dca-3de6-49c6-a864-df5749cbe55a">

```
db.query(Question).all()    # Question 객체(질문)을 전부 조회
db.query(Question).filter(Question.id==1).all()    # filter를 통해 조건 검색
db.query(Question).get(1)                          # id는 primary key(유일 값)이므로 get 함수로도 조회 가능
db.query(Question).filter(Question.subject.like("%FastAPI%")).all()    # subject 컬럼에 FastAPI라는 문자열이 포함된 Question객체 조회
```

- filter함수에 전달되는 like함수에 전달된 문자열에 붙은 % : 임의의 문자열을 나타냄
- %FastAPI (=FastAPI로 끝나는 문자열), FastAPI% (=FastAPI로 시작하는 문자열), %FastAPI% (=FastAPI를 포함하는 문자열)

<img width="300" alt="image" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/14e74596-7466-445e-a3d6-a96a330cfac4">
<img width="300" alt="image" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/268d08c0-c534-4b22-a610-1cd45ce2b809">

- id == 2 인 Question 객체의 subject 컬럼 값을 변경하고 조회해본 것이 좌측 사진이다
- id == 1 인 Question 객체를 삭제하고 Question 객체를 전부 조회하면 원래 2개에서 1개가 삭제되어 1개만 남은 것을 확인할 수 있다

<br>

<img width="500" alt="image" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/b9e076d1-d352-48f8-9b80-3a3f8c91752f">
<img width="400" alt="image" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/eada48fd-df1a-4afe-8ccf-b6a009e5edd9">

- Answer 객체에 id가 자동적으로 1이 주어진 것을 확인할 수 있으며 이를 통해 get 함수로도 조회할 수 있다
- a에 할당된 Answer 객체를 생성할 때 "question=q"를 하여 relationship이 정의되었다
- relationship에 따라 a.question로 answer가 할당된 Question 객체를 조회할 수 있다
- relationship의 backref에 "answers"라 하였기 때문에, q.answers를 사용해서 Answer 객체인 a를 조회할 수 있다

```shell
from datetime import datetime
from models import Question, Answer
from database import SessionLocal
db = SessionLocal()
q = db.query(Question).get(2)
a = Answer(question=q, content='네 자동으로 생성됩니다.', create_date=datetime.now())
db.add(a)
db.commit()

a = db.query(Answer).get(1)
a
a.question    # a가 답한 Question 객체 q를 조회
q.answers     # q에 대답한 Answer 객체 a를 조회(여러 Answer 객체가 있었다면 해당 객체들 모두 조회)
```

<br>

## 4. 질문 목록 API 만들기

### 라우터
<img width="900" alt="image" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/4f7a3ad9-01d7-4fc4-9049-bbaa2d6dcf68">

```
# myapi에서
uvicorn main:app --reload    # FastAPI 서버 실행(백엔드 서버)

# myapi/frontend에서
npm run dev                  # Svelte 서버 실행(프론트엔드 서버)
```

<br>

<img width="700" alt="image" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/d4e31bd9-2227-4438-a9b7-3998ffae358d">
<img width="500" alt="image" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/09701689-f27f-437b-92e4-6c350c7a849c">

```python
# domain/question/question_router.py 생성

from fastapi import APIRouter

from database import SessionLocal
from models import Question

router = APIRouter( # APIRouter 클래스로 생성한 router 객체
    prefix = "/api/question",   # prefix : 요청 URL 앞부분에 항상 포함되어야 하는 값
)

@router.get("/list")    # /api/question/list라는 URL 요청에 대응
def question_list():
    db = SessionLocal()
    _question_list = db.query(Question).order_by(Question.create_date.desc()).all()
    db.close()
    return _question_list
```

```python
# main.py 수정

from domain.question import question_router # ./domain/question/question_router.py를 포함
app.include_router(question_router.router) # question_router 파일의 router 객체를 포함
```

<br>

### 의존성 주입

- 질문 목록 API를 작성하였으니 프론트엔드에서 질문 목록 API를 호출하여 결과값을 화면에 출력할 수 있을 것이다
- 그러나 question_list 함수에서 db 세션 객체를 생성하고 db.close()를 호출하는데 이를 자동화해야 한다
    - cf) db.close()를 수행하지 않으면 SQLAlchemy가 사용하는 컨넥션 풀에 db 세션이 반환되지 않아 문제가 생긴다

<img width="450" alt="image" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/2dc9a153-9c49-4c85-9891-df8c22413720">
<img width="450" alt="image" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/8e9a3d23-4658-4750-8499-ff2abb2d6d78">

- 위와 같이 database에서 get_db라는 generator 함수를 만들고 question_router.py에서 with 구문으로 이를 활용하면, 안전한 코드를 설계할 수 있다
- db.close()는 with 구문이 끝나면서 오류의 여부와 상관없이 실행되어 컨넥션 풀에 세션을 반납할 수 있게 된다

<br>

<img width="644" alt="image" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/2f0337b5-feda-4d25-a267-7e9ebaa5697f">

- with 구문을 사용하는 대신, db : Session = Depend(get_db)를 사용해서 의존성 주입을 할 수 있다
- db 객체가 Session 타입임을 지정하고, db에는 get_db로 생성된 세션 객체가 주입된다
- 이 때 get_db 함수에 자동으로 contextmanager가 적용되기 때문에 database.py의 get_db 함수에서 @contextlib 부분을 제거해야 한다

<br>

### 스키마

- 현재 질문 목록 API의 출력은 all()로 Question 모델의 모든 항목을 출력으로 리턴하고 있다
- 하지만 외부로 공개되면 안 되는 출력 항목이 있을 수 있고 출력값이 정확한지 검증하고 싶을 수도 있다
- 이럴 때 사용하는 것이 Pydantic 라이브러리이다
- Pydantic : FastAPI의 입출력 스펙을 정의하고 그 값을 검증하기 위해 사용하는 라이브러리

```python
# myapi/domain/question/question_schema.py
import datetime

from pydantic import BaseModel

class Question(BaseModel): # BaseModel을 상속한 Question 객체 --> Question Schema
    id : int
    subject : str | None = None     # subject 값이 Null일 수 있음을 구현 --> nullable=True
    content : str
    create_date : datetime.datetime

# 추가로 question_router.py 수정
from domain.question import question_schema 
@router.get("/list", response_model=list[question_schema.Question]) # response_model로 Question 스키마로 구성된 리스트를 설정
```

- Pydantic의 BaseModel을 상속받은 Question 스키마를 생성한다
- "str | None = None"은 None 값을 허용하는 것으로 subject 컬럼의 nullable=True에 맞게 구현한 부분이다
- @router.get에 response_model 속성을 추가하여 출력되는 데이터를 제한하거나 값을 검증하게 하였다

<br>

## 5. 질문 목록 화면 만들기

### 질문 목록 화면 구현하기

- 질문 목록 API를 호출하여 그 내용을 웹 브라우져에 표시하도록 만들 예정이다
- 이를 위해서는 프론트엔드 코딩이 필요하며, myapi/frontend/src/App.svelte를 다음과 같이 수정해야 한다

```html
<script>  // script 안에서는 Javascript 코드를 작성
  let question_list = []  // 리스트 변수를 선언

  function get_question_list() {
    fetch("http://127.0.0.1:8000/api/question/list").then((response) => { // fetch로 서버에 GET 요청을 보내고
      response.json().then((json) => {  // 응답 받은 후 JSON으로 변환
        question_list = json            // 콜백 함수에서 받은 JSON 데이터를 question_list에 저장
      })
    })
  }
  get_question_list()
</script>

<ul>  <!-- unordered list 태그 -->
  {#each question_list as question} <!-- #each로 반복문 구현 --> 
    <li>{question.subject}</li> <!-- li : list item 태그, question 객체의 subject 속성-->
  {/each}
</ul> <!-- unordered list에서 list item이 수직으로 쌓여 나가서 Question 객체의 subject가 순차적으로 표시 -->
```

<img width="557" alt="image" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/af84158b-fed4-46f7-90d5-993d9ee01bcf">

- 질문 목록 API를 통해 현재 Question 객체로 DB에 저장된 1개의 데이터의 subject("FastAPI Model Question")이 출력되었다

<br>

### Svelte Router

- 질문 답변 사이트인 파이보(pybo)는 다음과 같은 화면들이 필요하다
  1. 질문 목록 - 질문의 목록을 표시하는 화면
  2. 질문 상세 - 질문의 상세 내용을 확인하고 답변을 작성하는 화면
  3. 질문 작성 - 질문을 작성하는 화면
  4. 질문 수정 - 질문을 수정하는 화면
  5. 답변 수정 - 답변을 수정하는 화면
  6. 회원 가입 - 회원 가입을 위한 화면
  7. 로그인 - 로그인을 위한 화면

- Svelte는 SPA(Single Page Application)이기 때문에 단 하나의 페이지에서만 내용을 달리하여 표시해야 한다
    - cf) SPA :  웹 사이트의 전체 페이지를 하나의 페이지에 담아 동적으로 화면을 바꿔가며 표현하는 것
- 하나의 페이지에서 화면을 바꾸어가며 만들려면 코드가 복잡해지나 svelte-spa-router를 사용하면 된다

<img width="450" alt="image" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/dc73a42c-640c-424a-ac1a-a7514f2ba36a">

```bash
# myapi/frontend 에서
npm install svelte-spa-router    # svelte-spa-router 설치
npm run dev                      # 설치 후 서버 재시작
```

<br>

<img width="900" alt="image" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/61bcb256-6d88-407c-8476-d199f9459ff8">

- myapi/frontend/src 하위에 routes 디렉토리를 만들어서 필요한 화면들 각각에 대한 URL 주소를 매핑하는 파일들을 따로 관리한다
- Home.svelte에 기존의 App.svelte 내용을 복사하고 App.svelte는 svelte-spa-router의 Router 컴포넌트를 생성하도록 수정한다
- 이를 통해 정의한 라우팅이 애플리케이션에서 적용하여 페이지의 경로에 따라 다른 컴포넌트를 표시할 수 있도록 한다

<br>

### API 호출 라이브러리

- 질문 목록처럼 데이터를 조회하기 위해서는 항상 백엔드 서버에 요청하여 데이터를 가져와야 한다
- fetch함수를 사용하는 부분을 공통 라이브러리로 만들어서 사용하면 편리할 것이다

- myapi/frontend/src/lib에 api.js 파일을 다음과 같이 생성한다

```javascript
/* 파라미터 설명
operation : 데이터를 처리하는 방법(get, post, put, delete)
url       : 요청 URL, 단 백엔드 서버의 호스트명 이후의 URL만 전달
params    : 요청 데이터     ex) {page : 1, keyword : "마크다운"}
success_callback : API 호출 성공시 수행할 함수, API 호출시 반환된 JSON이 입력으로 주어짐
failure_callback : API 호출 실패시 수행할 함수, 오류값이 입력으로 주어짐
*/
const fastapi = (operation, url, params, success_callback, failure_callback) => {
    let method = operation
    let content_type = 'application/json'
    let body = JSON.stringify(params) // 요청 데이터를 JSON 문자열로 바꿔서 body로 저장

    // let _url = 'http://127.0.0.1:8000'+url  // url 파라미터는 호스트명을 생략하도록
    let _url = import.meta.env.VITE_SERVER_URL+url // .env 파일에 등록한 환경변수를 사용

    if(method === 'get') { // GET이면
        _url += "?" + new URLSearchParams(params)  // 파라미터를 GET 방식에 맞게끔 조립
    }

    let options = {
        method: method,
        headers: {
            "Content-Type": content_type
        }
    }

    if (method !== 'get') { // GET이 아니면
        options['body'] = body // options에 body 항목에 전달 받은 요청 데이터(params의 JSON형태) 추가
    }

    fetch(_url, options)
        .then(response => {
            response.json()
                .then(json => { // API 호출 성공은 HTTP 프로토콜의 응답코드가 200~299이므로
                    if(response.status >= 200 && response.status < 300) {  // 200 ~ 299
                        if(success_callback) {
                            success_callback(json)
                        }
                    }else {
                        if (failure_callback) {
                            failure_callback(json)
                        }else { //failure_callback이 없어도 alert로 오류 부분 출력
                            alert(JSON.stringify(json))
                        }
                    }
                })
                .catch(error => {
                    alert(JSON.stringify(error))
                })
        })
}

export default fastapi // 해당 모듈을 다른 파일에서 가져올 수 있도록 내보내기(export)
```

<br>

- 호스트명을 하드코딩(http://127.0.0.1:8000)한 상황인데, 호스트명은 개발, 운영 등 상황에 따라 변하니 하드코딩된 상태는 좋지 않다
- 따라서 호스트명을 따로 환경파일에 저장하고 그 값을 불러와 사용할 수 있도록 수정하도록 한다
- 이를 위해 myapi/frontend에 .env 파일을 생성하고 VITE_SERVER_URL 환경변수를 추가한다
    - svelte 파일에서 .env 파일의 항목을 읽기 위해서는 반드시 VITE_로 시작하는 환경변수명을 등록해야 한다
- 그리고 등록한 환경변수를 사용하도록 api.js파일의 _url 변수를 수정해준다
- 또한 Home.svelte에서 api.js의 fastapi 함수를 사용하도록 코드를 수정한다

```
# myapi/frontend/.env 파일 생성
VITE_SERVER_URL=http://127.0.0.1:8000
```

```svelte
// myapi/frontend/src/routes/Home.svelte 수정
<script>  // script 안에서는 Javascript 코드를 작성
    import fastapi from "../lib/api" // myapi/frontend/src/lib/api.js 파일의 fastapi 함수를 import
    let question_list = []  // 리스트 변수를 선언
  
    function get_question_list() {
        fastapi('get', '/api/question/list', {}, (json) => {
            question_list = json
        }) // operation으로 GET, url을 주고 params는 빈 값, success_callback으로 화살표 함수, failure_callback은 생략
           // success_callback은 응답으로 받은 json 데이터를 question_list에 대입하라는 내용
           // failure_callback은 없어도 alert로 오류 내용을 표시하게 되어 있으니 괜찮다
    }
    get_question_list()
</script>

<ul> <!-- unordered list 태그 -->
    {#each question_list as question} <!-- #each로 반복문 구현 --> 
        <li>{question.subject}</li> <!-- li : list item 태그, question 객체의 subject 속성-->
    {/each}
</ul> <!-- unordered list에서 list item이 수직으로 쌓여 나가서 Question 객체의 subject가 순차적으로 표시 -->
```

<br>

## 6. 질문 상세

```javascript
// myapi/frontend/src/routes/Home.svelte 수정

import { link } from 'svelte-spa-router' // a 태그에 use:link 속성을 사용하기 위해
<li><a use:link href="/detail/{question.id}">{question.subject}</a></li> 
```

```javascript
// myapi/frontend/src/App.svelte 수정

import Detail from "./routes/Detail.svelte"

const routes = {
    '/' : Home,     // '/' 주소에 매핑되는 컴포넌트로 <Home />을 등록 --> Home.svelte 파일의 내용
    '/detail/:question_id' : Detail, // :question_id처럼 앞에 :가 있으면 가변적인 값이 올 수 있음을 의미한다
}
```

```javascript
// myapi/frontend/src/routes/Detail.svelte 생성

<script>
    export let params = {}
    let question_id = params.question_id
    console.log('question_id:' + question_id)
</script>

<h1>제목</h1>
<div>
    내용
</div>
```

<img width="479" alt="image" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/29b8fc53-0aad-4032-8942-4352cbc4c11d">

1. 질문 목록으로 출력한 제목 부분에 링크를 추가하기 위해 Home.svelte에 { link }를 import하고 코드를 수정한다
2. detail에 관한 URL 규칙을 등록하기 위해 App.svelte 파일의 routes 객체를 위와 같이 수정한다
3. Detail.svelte를 추가하여 질문 목록 중 하나를 누르면 http://127.0.0.1:8000/#detail/2와 같은 URL이 호출되고 전달된 파라미터 question_id가 콘솔에 잘 출력되는지 확인한다

<br>

```python
# myapi/domain/question/question_crud.py에 함수 추가

def get_question(db : Session, question_id : int):  # Path Parameter인 question_id를 받아서 
    question = db.query(Question).get(question_id)  # 해당 Question 객체를 반환
    return question
```

```python
# myapi/domain/question/question_router.py에 함수 추가

@router.get("/detail/{question_id}", response_model=question_schema.Question)   # 리턴은 하나의 Question 객체
def question_detail(question_id : int, db : Session = Depends(get_db)):  # path parameter 'question_id' 받음
    question = question_crud.get_question(db, question_id = question_id) # crud.py에서 정의한 함수로 해당 question_id로
    return question                                                      # Question 객체를 조회해서 반환
```

```javascript
// myapi/frontend/src/routes/Detail.svelte 수정

<script>
    import fastapi from "../lib/api"

    export let params = {} // Detail 컴포넌트를 호출할 때 전달한 파라미터 값을 params에 읽어오기
    let question_id = params.question_id
    let question = {}

    function get_question() {   // 읽어온 question_id로 detail/:question_id 꼴로 요청을 보내
        fastapi("get", "/api/question/detail/" + question_id, {}, (json) => {  
            question = json     // JSON 형태로 데이터를 받고 이를 question 변수에 저장한다
        })
    }

    get_question()
</script>

<!-- 저장한 question 변수에서 subject와 content를 꺼내서 출력한다-->
<h1>{question.subject}</h1>     
<div>
    {question.content}
</div>
```

<img width="450" alt="image" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/2d359207-971e-4653-a528-a689d581f648">
<img width="450" alt="image" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/baddc218-a99f-4a47-a4d3-672aa8155020">

<br>

4. 질문 상세 화면을 프론트 단위에서 구성했으니, 백엔드 영역에서 질문 한개에 대한 상세 내용을 리턴하는 질문 상세 API를 작성해야 한다
5. question_crud.py에 get_question 함수를 추가하여 path parameter로 question_id를 받아 해당 키를 갖고 있는 Question 객체를 DB에서 조회해서 반환한다
6. FastAPI의 docs 문서에서 새로 만든 질문 상세 조회 API를 테스트하면 위의 좌측 사진과 같다
7. 질문 상세 API가 준비되었으니, 마지막으로 Detail.svelte를 수정하여 기존에 "제목", "내용"에 해당 Question 객체의 subject와 content를 출력할 수 있게 한다

<br>

## 7. 답변 등록

- 앞에서 기존에 있는 질문 목록과 상세 내역을 조회하는 기능을 만들었다 (GET method)
- 이번에는 질문에 답변을 등록하고 등록한 답변을 보여주는 기능을 만든다 (POST method)


### 답변 등록 API

```python
# myapi/domain/answer/answer_schema.py 생성

from pydantic import BaseModel, field_validator

class AnswerCreate(BaseModel):  # 답변 등록시 사용할 스키마
    content : str               # 답변 등록에 전달되는 유일한 파라미터, 유일하기에 필수값(nullable=False)

    @field_validator('content')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError("빈 값은 허용하지 않습니다.")
        return v
```

```python
# myapi/domain/answer/answer_crud.py 생성

from datetime import datetime
from sqlalchemy.orm import Session
from domain.answer.answer_schema import AnswerCreate
from models import Answer, Question

# 답변을 등록하기 위한 create_answer 함수
# db와 Question 객체, AnswerCreate 객체를 받아서 모델 중 하나인 Answer 객체를 만들고 이를 db에 올린다
def create_answer(db : Session, question: Question, answer_create : AnswerCreate):
    db_answer = Answer(question = question,
                       content = answer_create.content,
                       create_date = datetime.now())
    db.add(db_answer)
    db.commit()
```

```python
# myapi/domain/answer/answer_router.py 생성

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from database import get_db
from domain.answer import answer_schema, answer_crud
from domain.question import question_crud

router = APIRouter(
    prefix = "/api/answer",
)

@router.post("/create/{question_id}", status_code=status.HTTP_204_NO_CONTENT)
def answer_create(question_id : int,    # path parameter인 question_id
                  _answer_create : answer_schema.AnswerCreate,
                  db : Session = Depends(get_db)):
    question = question_crud.get_question(db, question_id=question_id) # question_id로 Question 조회

    if not question: # 만약 해당하는 question이 없다면
        raise HTTPException(status_code=404, detail="Question not found") # '응답 없음'을 출력
    answer_crud.create_answer(db, question=question,        # question이 있으면 이에 대한
                              answer_create=_answer_create) # Answer 객체를 생성하고 db에 올린다(함수 내부적으로)

```

```python
# myapi/main.py에 answer_router를 추가
from domain.answer import answer_router

# ... 중간 생략

app.include_router(answer_router.router)
```

1. answer_schema.py를 생성하여 답변 등록시 사용할 스키마를 정의한다
2. answer_crud.py를 생성하여 POST method에 맞는 create_answer 함수를 정의한다
    - cf) create_answer 함수 : db, Question, AnswerCreate 객체를 받아서 Answer 객체를 만들고 DB에 올리는 함수
3. answer_router.py를 생성하여 APIRouter 객체를 생성하고 path parameter인 question_id로 Question 객체를 조회하고 이를 바탕으로 answer_crud의 create_answer 함수를 호출하여 Answer 객체를 생성하고 DB에 올리는 작업을 수행한다
4. 작성한 router를 main.py에 등록한다 

<br>

### 답변 등록 화면 작성

<img width="626" alt="image" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/97fc7854-1b1c-489f-b76d-97c3a6031aa0">

```javascript
# myapi/frontend/src/routes/Detail.svelte 수정

<script>
    import fastapi from "../lib/api"

    export let params = {} // Detail 컴포넌트를 호출할 때 전달한 파라미터 값을 params에 읽어오기
    let question_id = params.question_id
    let question = {}
    let content = ""

    // 하나의 질문을 가져오는 함수
    function get_question() {   // 읽어온 question_id로 detail/:question_id 꼴로 요청을 보내
        fastapi("get", "/api/question/detail/" + question_id, {}, (json) => {  
            question = json     // JSON 형태로 데이터를 받고 이를 question 변수에 저장한다
        })
    }

    get_question()

    // 답변을 등록하는 함수
    function post_answer() {
        event.preventDefault()  // submit 버튼이 눌릴 경우 form이 자동으로 전송되는 것을 방지
        let url = "/api/answer/create/" + question_id
        let params = {
            content : content
        }
        fastapi('post', url, params, 
            (json) => {
                content = ''
                get_question()
            }
        )
    }
</script>

<!-- 저장한 question 변수에서 subject와 content를 꺼내서 출력한다-->
<h1>{question.subject}</h1>     
<div>
    {question.content}
</div>

<form method="post">
    <textarea rows="15" bind:value={content}></textarea> <!--글을 적는 공간을 만들고 content에 저장-->
    <input type="submit" value="답변 등록" on:click="{post_answer}"> <!-- '답변 등록' 버튼을 누르면 post_answer함수 실행-->
</form>
```

5. 답변 등록 API는 응답 결과가 없는 API인데 기존에 fastapi 함수는 응답결과(json)가 있을 경우에만 success_callback을 실행하므로 수정을 해줘야 한다
    - response.status가 204(No content)인 경우에 success_callback을 호출하고 뒤의 코드가 실행되지 않도록 return 처리한다
6. Detail.svelte를 수정하여 답변 입력을 위한 텍스트 창(textarea), <답변등록> 버튼, 버튼을 누르면 답변을 등록하는 post_answer 함수를 구현한다

<br>

### 질문 상세의 출력 스키마 수정(Answer, Question)

```python
# myapi/domain/answer/answer_schema.py에 추가

class Answer(BaseModel):    # Answer 스키마는 출력으로 사용할 답변 1건을 의미
    id : int
    content : str
    create_date : datetime.datetime
```
```python
# myapi/domain/question/question_schema.py 수정

from domain.answer.answer_schema import Answer

class Question(BaseModel): # BaseModel을 상속한 Question 객체 --> Question Schema
    id : int
    subject : str | None = None     # subject 값이 Null일 수 있음을 구현 --> nullable=True
    content : str
    create_date : datetime.datetime
    answers : list[Answer] = []     # Question 모델과 Answer 모델은 relationship으로 연결되어 있다
                                    # backref="answers"이므로 반드시 "answers"라는 이름의 속성으로 추가해야 한다
```

<img width="637" alt="image" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/6e9afbca-4c5b-48cf-bb33-4fb1f7a9526a">

7. answer_schema.py에 출력으로 사용할 답변 1건에 대한 Answer 스키마를 추가한다
8. question_schema.py의 Question 스키마에 Answer 스키마로 구성된 answers 리스트를 추가한다
    - Question 모델은 Answer 모델과 relationship으로 연결되어 있으며 backref="answers"이므로 반드시 answers라는 이름의 속성을 사용해야 한다

<br>

### 질문 상세 화면에 답변 표시하기

```javascript
// myapi/frontend/src/routes/Detail.svelte 수정

<script>
// ... 생략
    let question = {answers:[]} // each문에서 question.answers를 참조하고 있는데
                                // get_question은 비동기로 진행되므로
                                // 아직 조회되지 않은 상태에서 each문이 실행되면 answers 항목이 없어서 오류 발생
// ... 생략
</script>

<!-- 질문에 등록된 답변(answers)들을 순차적으로 표시하는 부분 -->
<ul>
    {#each question.answers as answer}
        <li>{answer.content}</li>
    {/each}
</ul>
```

9. Detail.svelte를 수정하여 질문에 등록된 답변들을 화면에 표시한다 
    - #each 반복 구문과 <li> 태그를 사용해서 순차적으로 쌓는 방식으로 일단 표현한다

<br>

### 오류 처리하기

<img width="450" alt="image" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/d8859f8c-427a-41a5-afb6-f479e223bef4">
<img width="300" alt="image" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/58a670cd-86cd-454e-8027-8768567fa443">

```javascript
# myapi/frontend/src/components/Error.svelte 추가
<script>
    export let error // 전달 받은 오류
</script>

{#if typeof error.detail === 'string'}
    <ul>
        <li>{error.detail}</li>
    </ul>
{:else if typeof error.detail === 'object' && error.detail.length > 0}
    <ul>
        {#each error.detail as err, i}
        <li>
            <strong>{err.loc[1]}</strong> : {err.msg}
        </li>
        {/each}
    </ul>
{/if}
```

```javascript
# myapi/frontend/src/routes/Detail.svelte 수정

<script>
import Error from "../components/Error.svelte" // 오류 처리를 위해
let error = {detail : []}

// ... 생략

// 답변을 등록하는 함수
    function post_answer() {
        event.preventDefault()  // submit 버튼이 눌릴 경우 form이 자동으로 전송되는 것을 방지
        let url = "/api/answer/create/" + question_id
        let params = {
            content : content
        }
        fastapi('post', url, params, 
            (json) => { // success_callback
                content = ""
                error = {detail : []}   // 오류가 발생한 이후 다시 입력값을 조정하여 성공했을 때를 위해
                                        // error를 다시 초기화 해줘야 의도한 바대로 출력된다
                get_question()
            },
            (err_json) => { // failure_callback
                error = err_json
            }
        )
    }
</script>

// ... 생략

<!-- 오류 발생시 오류의 내용을 확인할 수 있도록 -->
<Error error={error} />

// ... 생략
```

10. 답변을 등록하는 텍스트 창(Textarea)에 값을 넣지 않고 '답변등록' 버튼을 누르면, fastapi를 호출할 때 failure_callback 함수를 전달하지 않았기 때문에 alert 창이 표시된다
11. myapi/frontend/src 하위에 Error 컴포넌트를 저장할 components 디렉토리를 만들고 위와 같이 Error.svelte 파일을 생성한다
12. Detail.svelte의 post_answer 함수에 failure_callback에 에러를 JSON 형식으로 받도록 설정하고 Error 컴포넌트의 error 변수에 이를 보내서 화면에 출력할 수 있도록 한다

<br> 

<img width="450" alt="image" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/717067a8-9d37-4e14-937d-5872aec625d3">
<img width="450" alt="image" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/97140357-fc7e-4600-b7d6-633e0a320340">

- "content : Value error, 빈 값은 허용하지 않습니다."라고 오류의 내용이 alert창이 아닌 Error 컴포넌트로 표시되는 것을 확인할 수 있다
- 그대로 특정 문자열("빈 값이 아닙니다")을 입력하고 답변 등록을 하면, 에러 출력 없이 답변 목록이 늘어나는 것도 확인할 수 있다
    - success_callback에서 error = {detail : []}로 초기화해주기 때문에 오류 메시지 없이 답변 목록만 늘어나는 것이다

<br>

## 8. 화면 예쁘게 꾸미기

<br>

## 9. 부스트랩으로 더 쉽게 화면 꾸미기

<br>

## 10. 질문 등록

<br>

# 3장. 파이보 서비스 개발

<br>

# 4장. 세상에 선보이는 파이보 서비스
