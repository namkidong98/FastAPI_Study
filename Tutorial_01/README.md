참고자료: https://www.youtube.com/playlist?list=PLqAmigZvYxIL9dnYeZEhMoHcoP4zop8-p Part 1~2

## Python Version 확인 & 가상 환경 설정

<img width="600" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/627d9ece-dbc2-49dd-8e06-abbf8b3b66fe">   

```
python -m venv env     # 현재 디렉토리에 env라는 이름의 가상 환경이 생성
```
- 생성된 가상 환경은 프로젝트에 필요한 Python 패키지 및 의존성을 격리된 환경에서 관리할 수 있게 해준다

<br> 

## requirements.txt & install

<img width="600" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/98fb4ead-7f5d-46b7-b68c-cc95eb61bbbc">

- fastapi와 uvicorn을 requirements.txt에 포함하고 다음 명령어를 실행시킨다

```
pip install -r requirements.txt   
```
- requirements.txt : 프로젝트에 필요한 모든 패키지와 그 버전 정보를 정의한 파일
- -r 옵션을 사용하여 해당 파일의 내용을 읽어 필요한 패키지들을 설치
- uvicorn : ASGI(Asynchronous Server Gateway Interface) 애플리케이션을 위한 빠르고 경량의 웹 서버

<br> 

## 기본 코드 예제

<img width="700" alt="스크린샷 2024-01-08 093854" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/53de6677-6362-423f-a1ea-91ef215c53f4">

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"messeage" : "hello world"}
```
- uvicorn main:app --reload을 통해 main.py 파일의 app(ASGI 애플리케이션 객체 이름)에 맞추어 서버를 구축(ASGI 애플리케이션을 실행)
- --reload: 코드 변경을 감지하여 서버를 자동으로 다시 시작하도록 하는 옵션, 개발 중에 코드를 수정하고 테스트할 때 특히 유용


<br> 

## Swagger Docs
- Swagger Docs : API 문서를 작성하고 표시하기 위한 도구 중 하나
- Swagger Docs의 역할 : 자동 문서 생성, 인터랙티브한 UI 제공, 코드 예제 제공, 표준화된 API 문서, API 버전 관리

<img width="646" alt="스크린샷 2024-01-08 094139" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/f720d644-c7a5-4efb-8313-1d736d2e130a">


<br> 

## HTTP 메소드와 REST API

- GET : 리소스를 조회하기 위해 사용되는 메서드, 주로 데이터를 가져오는 데 사용
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}
```

- POST : 리소스를 생성하기 위해 사용되는 메서드, 클라이언트가 서버로 데이터를 전송하여 새로운 리소스를 만들 때 사용
```python
from fastapi import FastAPI

app = FastAPI()

@app.post("/items/")
def create_item(item: dict):
    return item
```

- PUT : 리소스를 업데이트하기 위해 사용되는 메서드, 클라이언트가 서버로 데이터를 전송하여 기존 리소스를 업데이트할 때 사용
```python
from fastapi import FastAPI

app = FastAPI()

@app.put("/items/{item_id}")
def update_item(item_id: int, item: dict):
    return {"item_id": item_id, "updated_item": item}
```

- DELETE : 리소스를 삭제하기 위해 사용되는 메서드, 주로 클라이언트가 특정 리소스를 제거하고자 할 때 사용
```python
from fastapi import FastAPI

app = FastAPI()

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"message": f"Item {item_id} has been deleted"}
```

<br> 

## GET의 type check

- type이 int인 경우
  
<img width="517" alt="스크린샷 2024-01-08 094650" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/0e501a91-4218-4294-b588-d3e009f15edd">

- type이 str인 경우

<img width="521" alt="스크린샷 2024-01-08 094717" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/0c62a7a6-76e3-4485-9f1a-48a0a23141d8">

- 해당하는 type이 없는 경우

<img width="942" alt="스크린샷 2024-01-08 094637" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/c8b6d013-b342-4ff6-bc91-2f6eac2b7a4c">


<br> <br> 


## 코드 순서에 따른 작동 방식의 차이

<img width="600" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/fe1a573a-83ac-4b2c-9189-6a19ef5e3dec">

<br>

- /users/ 뒤에 user_id가 먼저 오는 경우, me가 들어와도 me에 할당된 message가 아니라 상위에 선언된 {user_id}에 걸려서 실행된다

<img width="600" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/1876a6ec-4ea3-4e65-b85f-82f6a4a72ea6">

- 순서를 바꾸어 /users/me를 상위에 두면, me에 할당된 message가 출력되는 것을 확인할 수 있다

