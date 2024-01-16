## Part13 : Response Model

<img width="850" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/71a00e59-adf8-4e22-88de-a0f9f485878f">

- response_model을 따로 설정하지 않고 UserBase로 request body인 user를 설정하고 user을 반환하면 password도 공개되는 문제가 생긴다
- 이를 해결하고자 UserBase를 상속받는 UserIn과 UserOut을 만드는데, UserIn에만 password를 추가한다
- 그렇게 하면 입력은 UserIn으로 받되 response_model을 UserOut으로 해서 출력되는 response body에는 password가 생략될 수 있다

<br>

```python
class Item(BaseModel):
    name : str
    description : Optional[str] = None
    price : float
    tax : Optional[float] = None
    tags : list[str] = []

items = {
    "foo" : {"name" : "Foo", "price" : 50.2},
    "bar" : {"name" : "Bar", "description" : "The bartenders", "price" : 2, "tax" : 20.2},
    "baz" : {"name" : "Baz", "description" : None, "price" : 50.2, "tax" : 10.5, "tags" : []}
}

@app.get("/items/", response_model=Item, response_model_exclude_unset=True)
async def read_item(item_id : Literal["foo", "bar", "baz"]):
    return items[item_id]
```

- 우선 Literal을 사용해서 foo, bar, baz 중 하나만 item_id(Query)로 받을 수 있게 제한한다
- 셋 중 하나를 받으면 위에서 선언한 items 딕셔너리의 key로 사용해서 value를 반환하게 한다

<br>

### response_model_exclude_unset 옵션

- 이 때 response_model_exclude_unset = True 옵션을 쓰면, items에 있는 그대로, 즉 없는 Field에 대해서는 생략하고 출력이 나온다
```json
##---------response_model_exclude_unset=True인 경우----------##
# 1. item_id == "foo"에 대한 output
{
  "name": "Foo",
  "price": 50.2
}

# 2. item_id == "bar"에 대한 output
{
  "name": "Bar",
  "description": "The bartenders",
  "price": 2,
  "tax": 20.2
}

# 3. item_id == "baz"에 대한 output
{
  "name": "Baz",
  "description": null,
  "price": 50.2,
  "tax": 10.5,
  "tags": []
}
```

<br>

- 그러나 해당 옵션이 없다면 items에 있는 값들에 해당하는 부분만 업데이트된, Item의 전체 Field가 반환된다
```json
##---------response_model_exclude_unset가 없는 경우----------##
# 1. item_id == "foo"에 대한 output
{
  "name": "Foo",
  "description": null,
  "price": 50.2,
  "tax": null,
  "tags": []
}

# 2. item_id == "bar"에 대한 output
{
  "name": "Bar",
  "description": "The bartenders",
  "price": 2,
  "tax": 20.2,
  "tags": []
}

# 3. item_id == "baz"에 대한 output
{
  "name": "Baz",
  "description": null,
  "price": 50.2,
  "tax": 10.5,
  "tags": []
}
```
### response_model_include 옵션
```python
@app.get("/items/{item_id}/name", response_model=Item, response_model_include={"name", "description"})
async def read_item_name(item_id : Literal["foo", "bar", "baz"]):
    return items[item_id]
```

- response_model_include로 name과 description를 주었으므로, item_id에 해당하는 items의 value에서 update할 부분을 하고
- 전체 Item의 Field 중 name과 description만 반환하는 구조이다

```json
##---------response_model_include 예제 ----------##
# 1. item_id == "foo"에 대한 output
{
  "name": "Foo",
  "description": null
}

# 2. item_id == "bar"에 대한 output
{
  "name": "Bar",
  "description": "The bartenders"
}

# 3. item_id == "baz"에 대한 output
{
  "name": "Baz",
  "description": null
}
```

### response_model_exclude 옵션

```python
@app.get("/items/{item_id}/public", response_model=Item, response_model_exclude={"tax"})
async def read_items_public_data(item_id : Literal["foo", "bar", "baz"]):
    return items[item_id]
```

- response_model_exclude로 tax를 주었으므로, item_id에 해당하는 items의 value에서 update할 부분을 하고
- 전체 Item의 Field 중 tax를 제외한, 즉 name, description, price, tags를 반환하는 구조이다

```json
##---------response_model_exclude 예제 ----------##
# 1. item_id == "foo"에 대한 output
{
  "name": "Foo",
  "description": null,
  "price": 50.2,
  "tags": []
}

# 2. item_id == "bar"에 대한 output
{
  "name": "Bar",
  "description": "The bartenders",
  "price": 2,
  "tags": []
}

# 3. item_id == "baz"에 대한 output
{
  "name": "Baz",
  "description": null,
  "price": 50.2,
  "tags": []
}
```

<br><br>

## Part14 : Extra Models

<img width="450" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/4b7ea085-7382-4111-a9cc-bd97257789bf">
<img width="450" alt="image" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/84c7ae0c-3fc6-4ed8-bfad-90ae62ca052b">
<img width="750" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/f72ebcd8-29ea-43f7-9d41-9e0c440daf03">

- UserBase를 바탕으로 USerIn, UserOut에 이어 UserInDB를 추가했다
- UserInDB는 hased_password가 추가된 것으로 fake_save_user에서 fake_password_hasher 함수로 만들어진 hased_password를 포함한다
- response_model이 UserOut이기 때문에 username, email, full_name만 있는 것을 확인할 수 있다
- user_saved 자체는 UserInDB 객체이므로 hashed_password를 갖고 있어서 terminal에 출력된 부분에서 확인할 수 있다   
  cf) BaseModel에서 .dict() 메소드는 권장하지 않고 대신 model_dump()를 사용하면 된다

<br>

<img width="750" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/6f4a7559-3c81-4ab3-a923-8947013cd0c5">

- 우선 "str = "plane""과 같은 방식으로 해당 데이터 타입에 값을 지정할 수 있다
- 또한 typing의 Union을 사용하여 response_model이 둘 중 하나의 응답 형태를 가질 수 있도록 설정할 수 있다
- item2가 선택되자 plane 형식인 PlaneItem이 response_model로 선택되어 반환된 것을 확인할 수 있다
