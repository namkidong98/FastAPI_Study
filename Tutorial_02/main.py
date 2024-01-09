from fastapi import FastAPI
from typing import Optional

# Optional : 함수의 반환 값이나 매개 변수로 사용되며, 해당 값이 존재할 수도 있고 존재하지 않을 수도 있는 상황을 표현
#            값이 없는 경우에는 None으로 반환

app = FastAPI()

fake_items_db = [{"itme_name" : "Foo"}, {"itme_name" : "Bar"}, {"itme_name" : "Baz"}]
@app.get("/items/list")
async def list_items(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip+limit]

@app.get("/items/{item_id}")
async def get_item(item_id: str, q: Optional[str] = None, short : bool = False):
    item = {"item_id" : item_id}
    if q:
        item.update({"q" : q}) # dictionary의 update method : 추가하거나 기존 값을 갱신하는데 사용 
    if not short:
        item.update({"description" : "This is the item"})
    return item

from pydantic import BaseModel
# BaseModel: 상속받은 모델은 클래스 변수로 데이터의 필드와 해당 필드의 유효성 검사 규칙을 정의 가능 

class Item(BaseModel):
    name : str
    description : Optional[str] = None
    price : float
    tax : Optional[float] = None
    #tax : float | None = None # python 3.9 version이라 오류 발생

@app.post("/items")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax" : price_with_tax})
    return item_dict

@app.put("/items/{item_id}")
async def create_item_with_put(item_id : int, item : Item, q : Optional[str] = None):
    result = {"item_id" : item_id, **item.dict()}
    if q:
        result.update({"q" : q})
    return result

from fastapi import Query

# @app.get("/items")
# async def read_items(q: Optional[list[str]] = Query(None, max_length=10)):
#     results = {"items" : [{"item_id" : "Foo"}, {"item_id" : "Bar"}]}
#     if q:
#         results.update({"q" : q})
#     return results

@app.get("/items")
async def read_items(q: Optional[list[str]] = Query(None)):
    results = {"items" : [{"item_id" : "Foo"}, {"item_id" : "Bar"}]}
    if q:
        results.update({"q" : q})
    return results

@app.get("/items_hidden")
async def hidden_query_route(hidden_query: Optional[str] = Query(None, include_in_schema=False)):
    if hidden_query:
        return {"hidden_query" : hidden_query}
    return {"hidden_query" : "Not found"}
