## Part3 : Query Parameter
- Part2에서 다룬 Path Parameter는 app.get(" ~~~ ")와 같이 경로를 설정함으로써 다른 입력에 따른 처리를 수행했다
- Part3에서 다루는 Query Parameter는 추가적인 파라미터인 Query를 통해 옵션이 포함된 입력에 따른 처리를 수행한다
- 물론 Query에 대해 URL도 만들어지지만, 옵션으로 줄 수 있다는 점에서 차별점이 있다고 볼 수 있다

<br> 

<img width="700" alt="스크린샷 2024-01-09 104328" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/470173e6-61f2-44a1-adcf-34dfb3c48a6d">

- skip과 limit이라는 Query Parameter를 조절함으로써 다른 출력이 나오는 것을 확인할 수 있다 

<br> 

<img width="350" alt="스크린샷 2024-01-09 104338" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/318796d9-5cc7-4b10-aebe-53b3b2fee072">
<img width="350" alt="스크린샷 2024-01-09 104345" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/ad23cc3e-e8ad-427c-99a2-9d384028ef1a">

- Swagger Docs를 통해 확인할 수 있듯, Query Parameter에 대한 URL은 '?' 뒤에 오는 key-value 쌍으로 전달된다

<br>

<img width="700" alt="스크린샷 2024-01-09 105208" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/6884e012-c4dd-442a-88f0-0f00dcb130a7">

- item_id를 Path Parameter로, q와 short를 Query Parameter로 받아서 출력을 결정한다
- typing 라이브러리의 Optional은 값이 없는 경우에는 None을 반환하는 기능을 수행한다
- "Optional[str] = None"은 python 3.10 이상부터 "str | None = None"으로 대체 가능하다

<br>

## Part4 : Request Body
- FastAPI에서 HTTP 요청의 본문을 나타내는 request body를 정의하는 방법은 Pydantic 모델을 사용하는 것이다
- Pydantic 모델을 이용하면 데이터 모델의 구조를 정의하고 이를 통해 입력 데이터의 유효성을 검사할 수 있다

<br>

<img width="850" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/8eab0085-8499-461f-bb91-ce1378c237ca">
<img width="400" alt="스크린샷 2024-01-09 111952" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/c1abb9bd-cefe-4fd5-8ca0-21130ad52e9d">

- POST 메소드에 request body를 채움으로써 item_dict를 위와 같이 구체적으로 설정하여 생성(create)할 수 있다 

<br>

<img width="850" alt="스크린샷 2024-01-09 112547" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/679ed69e-8f8b-4981-bd6d-ec7ee302391b">
<img width="400" alt="스크린샷 2024-01-09 112554" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/c4502004-0b62-4b16-a47c-ea392daf1ce8">

- Path Parameter(item_id), Query Parameter(q), request body(Item)을 모두 활용한 예제이다

<br>

## Part5 : Query Parameters and String Validations
- fastapi의 Query 객체를 통해 Query Parameters를 정의하고 검증하는데 사용할 수 있다

<img width="707" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/e39af30e-df0a-40ec-9804-06be4a965251">
<img width="422" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/276c89c9-04d4-4a32-ac51-3f862fe72887">

- max_length인 10보다 작은 foobar를 query로 주면 문제 없이 query가 추가되고 반환되는 것을 확인할 수 있다

<br>

<img width="992" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/3ef4b242-7ca3-48d1-92cd-3e4b15504dde">

- 그러나 max_Length보다 긴 "foobarfoobarfoobarfoobar"을 주면 에러가 발생하는 것을 확인할 수 있다


<br>


<img width="600" alt="스크린샷 2024-01-09 115402" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/ead9fe23-584d-4417-bfb3-3a485eebc48c">
<img width="250" alt="스크린샷 2024-01-09 115450" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/cc4c1d12-1b54-4d86-97b1-4b34ff11abca">
<img width="250" alt="스크린샷 2024-01-09 115501" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/dea2a74e-59f2-4f33-bec4-b89d903387a9">
<img width="250" alt="스크린샷 2024-01-09 115522" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/1d5b057e-da54-4f8c-aadc-4c1581fe80a1">

- regex를 통해 정규식을 통한 매칭 옵션을 부여하는 것도 가능하다
- 'fixe'는 mismatch로, 'fixed query'는 max_length를 초과해서 에러가 발생하고 'fixedquery'는 모든 조건을 만족해서 값이 제대로 반환되는 것을 확인할 수 있다

<br>

<img width="860" alt="스크린샷 2024-01-09 121413" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/5adca5c2-0d5d-476e-9290-ae07b711b1cc">
<img width="931" alt="스크린샷 2024-01-09 121622" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/5c708b35-dbd9-441c-b9c6-35ff1f592a3b">

- str을 list의 원소의 타입으로 설정해놓으면, 위의 사진과 같이 결과가 나온다

<br>



