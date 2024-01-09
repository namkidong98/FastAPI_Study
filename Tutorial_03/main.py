from fastapi import FastAPI, Query, Path, Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

##------------------ Part 06 ------------------##
@app.get("/items_validation/{item_id}")
async def read_items_validation(
    item_id : int = Path(..., title="The ID of the item to get"),   # Path 객체를 사용
                                                                    # ...은 기본값을 사용하지 않는 특수 표시
    q : Optional[str] = Query(None, alias="item-query"), # alias로 호출하는 이름을 변경
    size : float = Query(..., gt=0, lt=7.75)
):
    results = {"item_id" : item_id, "size" : size}
    if q:
        results.update({"q" : q})
    return results
##---------------------------------------------##

##------------------ Part 07 ------------------##
class Item(BaseModel):
    name : str
    description : Optional[str] = None # not required
    price : float
    tax : Optional[float] = None # not required

class User(BaseModel):
    username : str
    full_name : Optional[str] = None

@app.put("/items/{item_id}")
async def update_item(
    *,                      # item_id = ~ 이런 식으로 설정하는게 파이썬 문법상 맨 뒤에 와야하는데
                            # 그렇지 않아도 되도록 하기 위해 맨 앞에 *, 를 추가한다
    item_id : int = Path(..., title="The ID of the item to get", ge = 0, le = 150),
    q : Optional[str] = None,           # 선택 사항으로 설정해두고
    item : Optional[Item] = None,       # 아래에서 만약 None이 아닌 경우에는
                                        # update로 results에 추가하도록 설계함
    user : User = Body(..., embed=True)
):
    results = {"item_id" : item_id}
    if q:
        results.update({"q" : q})
    if item:
        results.update({"item" : item})
    if user:
        results.update({"user" : user})
    return results
##---------------------------------------------##

##------------------ Part 08 ------------------##
from fastapi import Body
from pydantic import Field

class Item(BaseModel):
    name : str
    description : Optional[str] = Field(
        None, title = "The description of the item", max_length = 300
    )
    price : float = Field(..., \
        gt=0, description="The price must be greater than zero.")
    tax : Optional[float] = None

@app.put("/part8/item/{item_id}")
async def update_item(item_id : int, item : Item=Body(...)):
    results = {"item_id" : item_id, "item" : item}
    return results
##---------------------------------------------##