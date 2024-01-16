## Part15 : Response Status Codes

<img width="500" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/6a150977-175f-43ce-9704-b065d1240176">
<img width="300" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/454df37e-dce9-49f8-a50b-7eedbb3000cb">
<img width="300" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/3ca032ef-36f2-4f8f-b36c-69e0e91cc9d5">
<img width="300" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/4b106371-8b57-475a-bf1d-f5a36725c032">

- status_code 옵션에서 원하는 status code를 지정할 수 있다
- https://developer.mozilla.org/en-US/docs/Web/HTTP/Status 이 사이트에서 각각의 status code의 의미를 찾아볼 수 있다
- fastapi의 status 라이브러리를 사용해서 직관적으로 status_code의 의미를 확인하면서 사용할 수도 있다

<br>

## Part16 : Form Fields
<img width="500" alt="image" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/ceb205c4-5b7a-42d0-a2b2-94eff18f625f">
<img width="900" alt="image" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/86c1dd19-9ca1-4c27-ae6f-a3ccee68ab76">
<img width="900" alt="image" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/b5a9ef94-cba1-4c67-bcf6-142baefc88ed">

- fastapi의 Form을 사용하면 Body를 사용할 때와 다르게 Form data를 처리할 수 있다
- Body는 기본적으로 JSON 데이터를 처리하며 "application/json" 형식으로 데이터를 전송한다
- Form은 Form 데이터를 처리하며 "application/x-www-form-urlencoded" 형식으로 데이터를 전송한다
- Form 데이터는 HTML 폼을 통해 사용자로부터 데이터를 수집하거나, 파일 업로드와 같은 특별한 경우에 사용된다
  
<br>

## Part17 : Request Files
<img width="750" alt="image" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/938ae53c-6c51-48ae-8d40-99e5a6be9d3a">

- 파일들은 Form data의 형태로 업로드 된다 (multipart/form-data라고 되어 있는 부분에서도 확인 가능)
- bytes = File(...)은 바이트의 형태로 파일을 읽고 내용을 전달한다
- 이러한 경우 전체 내용이 메모리에 저장되기 때문에 작은 크기의 파일들에 적합한 방식이다
- 위의 사진에서 to_be_uploaded의 파일 내용이 그대로 반환된 것을 확인할 수 있다
- 참고로 Optional이나 '| None'을 사용하는 구문을 활용하면 Docs에서 file upload button이 비활성화된다!
  
<img width="750" alt="image" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/2416e628-cc06-4fe9-ab4d-89f487ee552a">

- UploadFile을 사용하면 최대 크기 제한까지만 메모리에 저장되며 이를 초과하는 경우 디스크에 저장된다
- 또한 업로드 된 파일의 메타 데이터를 얻을 수 있다(filename, content_type, file 등)
- 또한 async 메소드를 활용할 수 있다(ex read(size) : 파일의 바이트 및 글자의 size를 읽는다)
- 위의 예시에서 to_be_uploaded의 파일 이름이 반환되었으며 terminal에서는 async 메소드를 활용하여 읽어진 파일 내용이 출력된 것을 확인할 수 있다

<br>

<img width="750" alt="image" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/20b7b916-df71-4d12-90d9-b2a471036e82">
<img width="450" alt="image" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/a9d7f919-6b0e-41ae-8b21-96a9035f49ea">
<img width="450" alt="image" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/a1a5b506-63b0-41b1-a506-44c60a58430f">

- 나아가 list를 사용하여 다중 파일 업로드를 위와 같이 사용할 수 있다

## Part18 : Request Forms and Files
