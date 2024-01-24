# 1장. FastAPI 개발준비!

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

```

### 모델을 이용해 테이블 자동으로 생성하기

<img width="450" alt="image" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/93636a9b-e9a6-4bb0-b349-402c26ad5639">
<img width="450" alt="image" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/c705d553-ed2a-4b3d-8779-29fbf283dbf2">

- alembic init migrations로 생성된, myapi 하위의 alembic.ini과 migrations 하위의 env.py를 위와 같이 수정한다
- alembic.ini에는 sqlalchemy.url을 연결한 DB 주소로 변경하고, env.py에는 models.py에서 설정한 Base 클래스를 넣어준다

<br>

## 3. 모델로 데이터 처리하기

<br>

## 4. 질문 목록 API 만들기

<br>

## 5. API 호출 라이브러리

<br>

## 6. 질문 상세

<br>

## 7. 답변 등록

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
