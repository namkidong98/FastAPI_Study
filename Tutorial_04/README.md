## Part9: Body - Nested Models

<img width="700" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/b90e8f7f-5945-4a16-b25d-d26268fa7f91">

- list, set과 같은 data type도 사용할 수 있으며 [ ___ ] 을 채워 넣어서 원소의 type을 체크하는 유효성 검사를 할 수 있다

```python
{
  "item_id": 123,
  "item": {
    "name": "string",
    "description": "string",
    "price": 0,
    "tax": 0,
    "tags": [     # list이기 때문에 중복된 값도 그대로 포함
      1,
      1,
      2
    ],
    "unique": [    # set의 기능에 맞게 hello는 두 개중 1개만 남음
      "world",
      "hello"
    ]
  }
}
```

<br>

<img width="700" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/1524eaf1-588f-4a37-a963-d854c295c8d6">

- Image 모델과 list를 사용해서 Nested Model의 예제를 위와 같이 만들 수 있다

```python
{
  "item_id": 123,
  "item": {
    "name": "string",
    "description": "string",
    "price": 0,
    "tax": 0,
    "tags": [],
    "unique": [],
    "image": [     # list의 형식으로 Image class를 여러개 넣을 수 있다
      {
        "url": "https://www.google.com/",    # HttpUrl로 url을 나타낼 수 있다
        "name": "Google"
      },
      {
        "url": "https://www.youtube.com/",
        "name": "Youtube"
      }
    ]
  }
}
```

<br>

<img width="700" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/9ec4c292-1cf6-42a0-af18-9e06a593f89b">

- Offer --> Item --> Image로 3개의 모델이 Nested 된 예제이다
- list를 활용하여 1개의 Offer에 Item이 2개 포함된 것을 확인할 수 있다  
```python
{
  "name": "offer",
  "description": "string",
  "price": 0,
  "items": [
    {
      "name": "a",
      "description": "string",
      "price": 0,
      "tax": 0,
      "tags": [],
      "unique": [],
      "image": [
        {
          "url": "https://www.google.com/",
          "name": "Google"
        }
      ]
    },
    {
      "name": "b",
      "description": "string",
      "price": 0,
      "tax": 0,
      "tags": [],
      "unique": [],
      "image": [
        {
          "url": "https://www.youtube.com/",
          "name": "Youtube"
        }
      ]
    }
  ]
}
```

<br>

<img width="700" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/b668185d-cb7e-4247-9805-ac35f76377f0">

- dict[int, float]은 key는 int형, value는 float형이어야 함을 의미한다

```python
{
  "1": 1,
  "2": 1.5,
  "3": 2
}
```

cf) 주의사항
```python
{
  1: 1,
  2: 1.5,
  3: 2
}
```
- 위와 같이 따옴표를 제거한 int형 그대로 key값으로 사용하면 오류가 발생한다
- JSON 표준에 따르면, key는 반드시 문자열(str)이어야 하고, Pydantic은 JSON 표준을 따르기 때문에, 따라서 request body에서는 문자열 키를 기대한다

<br><br>

## Part10: Declare Request Example Data

### 방법1 : 모델 안에 Config, schema_extra에 example을 작성 --> 제대로 작동하지 않음
```python
class Item(BaseModel):
    name : str
    description : Optional[str] = None
    price : float
    tax : Optional[float] = None

    # 방법1 - 제대로 작동하지 X
    class Config:
        scheme_extra = {
            "example" : {
                "name" : "Foo",
                "description" : "A very nice Item",
                "price" : 16.25,
                "tax" : 1.67
            }
        }
```

### 방법2 : 모델에서 Field 객체의 example 옵션을 사용

<img width="700" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/8367e0ac-82f2-4d9f-a64a-262baeee8c45">

<br>

### 방법3 : 각각의 함수에 대해 Body 객체 안에 example 옵션을 사용

<img width="700" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/3e54b2c7-f5e9-43ab-8c91-8e61fa3fef6f">

<br>

### 추가 : Body에 openapi_examples(example 말고)로 선언하면 Swagger Docs에서 examples 옵션이 활성화된다
- 강의에서는 examples만 해도 되었지만 이후 바뀌었는지 openapi_examples로 사용해야 제대로 작동하는 것을 확인했다
```python
@app.put("/items/{item_id}")
async def update_item(
    item_id : int,
    item : Item = Body( # 방법3 : Body 객체 안에 example 옵션을 사용
        ...,
        openapi_examples= {
            "normal" : {
                "summary" : "A normal example",
                "description" : "A __normal__ item works _correctly_",
                "value" : {
                    "name" : "Foo",
                    "description" : "A very nice Item",
                    "price" : 16.25,
                    "tax" : 1.67
                }
            },
            "converted" : {
                "summary" : "An example with converted data",
                "description" : "FastAPI can convert price 'strings' to actual 'numbers' automatically",
                "value" : {"name" : "Bar", "price" : "16.25"}
            },
            "invalid" : {
                "summary" : "Invalid data is rejected with an error",
                "description" : "Hello youtubers",
                "value" : {"name" : "Baz", "price" : "sixteen point two five"}
            }
        }
    )):
    results = {"item_id" : item_id, "item" : item}
    return results
```

<img width="450" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/ceb641c2-bfff-4f76-813c-9cf6a8a9a313">
<img width="450" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/a84bea0e-a1dc-4474-a06a-9813c4c5387f">
<img width="450" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/84ddaddc-d65f-4236-9832-b21394e37065">

<br><br>

## Part11: Extra Data Types





<br>

## Part12: 

