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

