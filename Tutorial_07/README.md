## Part19 : Handling Errors

### HTTPSException

<img width="450" alt="image" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/69e49abb-d8f8-4ad9-9a39-0d62d986ed8d">
<img width="450" alt="image" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/83f85e17-f525-4d81-afb0-8c45f4155a73">

- HTTPSException : HTTP 응답 코드와 해당 응답의 내용을 정의하는 데 사용
- 예를 들어, 클라이언트가 올바르지 않은 요청을 보내거나 권한이 없는 리소스에 접근하려고 할 때 HTTPException을 발생시켜 적절한 HTTP 응답을 생성
- 유효한 입력 'foo'가 들어왔을 때는 '200 OK'가 terminal 로그에 뜨고 해당하는 반환 값이 출력된다
- 하지만 유효하지 않은 입력이 들어왔을 때, HTTPSException이 일어나고 설정한 headers도 docs에서 확인할 수 있다

<br>

### Customize Exception Handlers

<img width="900" alt="image" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/d9a060ab-228a-44d9-8c75-8280fc544d71">

- UnicornException 클래스를 선언하고 만약 yolo가 들어온 경우 UnicornException을 일으킨다
- UnicornException에 대해서는 exception_handler를 통해 JSON 형태로 status_code 418과 message를 반환하도록 설정해두었다

<br>

### RequestValidationError
<img width="802" alt="image" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/406069cd-bc5c-447f-a061-3b1d533cd6ad">

- RequestValidationError : FastAPI에서 요청 유효성 검사 실패 시 발생하는 예외
- FastAPI는 자동으로 요청을 검증하고, 요청이 기대되는 형식과 일치하지 않을 때 RequestValidationError을 발생시킨다
- 주로 요청의 경로 매개변수, 쿼리 매개변수, 요청 본문 등에서 발생할 수 있다
- 위의 예제에서는 size가 int형인데 "abc"가 입력으로 들어와서 RequestValidationError가 override된 것에 따라 나타난 것을 확인할 수 있다

<br>

## Part20 : Path Operation


## Part21 : JSON Compatible Encoder

