from fastapi import FastAPI
from typing import Optional

# Optional : 함수의 반환 값이나 매개 변수로 사용되며, 해당 값이 존재할 수도 있고 존재하지 않을 수도 있는 상황을 표현
#            값이 없는 경우에는 None으로 반환

app = FastAPI()

fake_items_db = [{"itme_name" : "Foo"}, {"itme_name" : "Bar"}, {"itme_name" : "Baz"}]
@app.get("/items")
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