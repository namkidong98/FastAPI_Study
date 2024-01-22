## Part19 : Handling Errors

<img width="450" alt="image" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/69e49abb-d8f8-4ad9-9a39-0d62d986ed8d">
<img width="450" alt="image" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/83f85e17-f525-4d81-afb0-8c45f4155a73">

- 유효한 입력 'foo'가 들어왔을 때는 '200 OK'가 terminal 로그에 뜨고 해당하는 반환 값이 출력된다
- 하지만 유효하지 않은 입력이 들어왔을 때, HTTPSException이 일어나고 설정한 headers도 docs에서 확인할 수 있다

<br>

<img width="900" alt="image" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/d9a060ab-228a-44d9-8c75-8280fc544d71">

- UnicornException 클래스를 선언하고 만약 yolo가 들어온 경우 UnicornException을 일으킨다
- UnicornException에 대해서는 exception_handler를 통해 JSON 형태로 status_code 418과 message를 반환하도록 설정해두었다

<br>



## Part20 : Path Operation


## Part21 : JSON Compatible
