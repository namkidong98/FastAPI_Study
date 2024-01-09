## Part6 : Path Parameters & Numeric Validation

<img width="750" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/39cc9ea1-3c4d-4166-8d3c-7ae8cc9dc8bf">

- Path 객체를 사용해서 Path parameter를 구체적으로 설정할 수 있다
- ...은 FastAPI에서 기본값을 사용하지 않는다는 특수 표시로 사용된다
- Query 객체의 'alias' 옵션으로 Query Parameter인 q를 q 대신 alias로 설정한 'item-query'로 지칭해야 한다

<br>

<img width="750" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/7cdd7fae-ea5a-47bf-a456-3149f3240c7a">

- Query 객체를 사용해서 float 형의 새로운 query parameter인 size를 만들었다
- gt(greater than), lt(less than)과 같은 옵션을 적용하여 numeric validation을 체크할 수 있다
- size가 범위 안에 있는 경우 에러 없이 result가 반환되고, size가 범위 밖에 있을 경우 에러가 발생하는 것을 볼 수 있다

<br>

## Part7 : Body - Multiple Parameters

<img width="750" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/36ead336-e001-4db0-838f-0cf1a0f0fd4b">
<img width="500" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/9d9049e3-d352-4009-a70f-b97d435a92f6">

- BaseModel을 상속 받은 Item 클래스를 Request Body로 하고 Path, Query 객체로 parameter를 정의한 코드 예제이다
- validation에 맞게 값을 넣어주면 위와 같이 제대로 반환되는 것을 확인할 수 있다

<br>

<img width="750" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/c80fd436-b2ef-4ab5-9bdf-891c0295ff45">

```json
{
  "item_id": 55,
  "q": "hello",
  "user": {
    "username": "nam",
    "full_name": "kidong nam"
  }
}
```

- User이라는 새로운 클래스를 추가하고 Request Body로 추가했으며, Optional인 item은 제거하고 User만 값을 넣어서 실행
- item_id(path parameter), q(query parameter), user(request body)가 제대로 반환된 것을 확인할 수 있다

<br>

<img width="750" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/a12b8a40-29a7-48ea-976f-6c557b61be43">

- Body 객체를 사용해서 Request Body를 명시할 수 있다


```
# HTTP 요청에서 서버로 데이터를 전달하는 방식 3가지 정리
1. Path Parameter : URL의 일부로 데이터를 전달하여 특정 리소스를 식별하는 데 사용, Path 객체를 통해 설정
2. Query Parameter: URL의 끝에 ?를 사용하여 key-value 쌍으로 데이터를 전달하여 필터링, 정렬 등에 사용, Query 객체를 통해 설정
3. Request Body   : POST, PUT 등의 HTTP 메소드를 사용하여 데이터를 요청 본문(body)에 담아 서버로 전달, 주로 큰 양의 데이터나 구조화된 데이터를 전송할 때 사용
                    Body 객체를 사용하여 설정
```
