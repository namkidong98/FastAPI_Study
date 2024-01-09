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
