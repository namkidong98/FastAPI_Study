from fastapi import FastAPI, Query, Path, Body
from pydantic import BaseModel, Field, HttpUrl
from typing import Optional

app = FastAPI()

##------------------ Part 09 ------------------##
# class Image(BaseModel):
#     url : HttpUrl       # pydantic에서 improt
#     name : str

# class Item(BaseModel):
#     name : str
#     description : Optional[str] = None
#     price : float
#     tax : Optional[float] = None
#     #tags : list = []        # empty list to default
#     tags : list[int] = []    # 리스트 안의 원소들의 type을 제한하는 방법
#     unique : set[str] = set() # set의 구조도 포함할 수 있다
#     image : Optional[list[Image]] = None

# class Offer(BaseModel):
#     name : str
#     description : Optional[str] = None
#     price : float
#     items : list[Item]

# @app.put("/item/{item_id}")
# async def update_item(item_id : int, item : Item):
#     results = {"item_id" : item_id , "item" : item}
#     return results

# @app.post("/offers")
# async def create_offer(offer : Offer = Body(..., embed = True)):
#     return offer

# @app.post("/blah")
# async def create_some_blahs(blahs : dict[int, float]):
#     return blahs
##---------------------------------------------##

##------------------ Part 10 ------------------##
# class Item(BaseModel):
#     # 방법2 - 모델에서 Field 객체의 example 옵션을 사용
#     name : str                          # = Field(..., example="Foo")
#     description : Optional[str] = None  # Field(None, example="A very nice Item")
#     price : float                       # = Field(..., example=16.25)
#     tax : Optional[float] = None        # Field(None, example=1.67)

#     # 방법1 - 제대로 작동하지 X
#     # class Config:
#     #     scheme_extra = {
#     #         "example" : {
#     #             "name" : "Foo",
#     #             "description" : "A very nice Item",
#     #             "price" : 16.25,
#     #             "tax" : 1.67
#     #         }
#     #     }

# @app.put("/items/{item_id}")
# async def update_item(
#     item_id : int,
#     item : Item = Body( # 방법3 : Body 객체 안에 example 옵션을 사용
#         ...,
#         openapi_examples= {
#             "normal" : {
#                 "summary" : "A normal example",
#                 "description" : "A __normal__ item works _correctly_",
#                 "value" : {
#                     "name" : "Foo",
#                     "description" : "A very nice Item",
#                     "price" : 16.25,
#                     "tax" : 1.67
#                 }
#             },
#             "converted" : {
#                 "summary" : "An example with converted data",
#                 "description" : "FastAPI can convert price 'strings' to actual 'numbers' automatically",
#                 "value" : {"name" : "Bar", "price" : "16.25"}
#             },
#             "invalid" : {
#                 "summary" : "Invalid data is rejected with an error",
#                 "description" : "Hello youtubers",
#                 "value" : {"name" : "Baz", "price" : "sixteen point two five"}
#             }
#         }
#     )):
#     results = {"item_id" : item_id, "item" : item}
#     return results
##---------------------------------------------##

##------------------ Part 11 ------------------##
# from uuid import UUID
# from datetime import datetime, time, timedelta

# @app.put("/items/{item_id}")
# async def read_items(
#     item_id : UUID,
#     start_date : Optional[datetime] = Body(None),
#     end_date : Optional[datetime] = Body(None),
#     repeat_at : Optional[time] = Body(None),
#     process_after : Optional[timedelta] = Body(None)
# ):
        
#     start_process = start_date + process_after
#     duration = end_date - start_process 

#     return {
#         "item_id" : item_id,
#         "start_date" : start_date,
#         "end_date" : end_date,
#         "repeat_at" : repeat_at,
#         "process_after" : process_after,
#         "start_process" : start_process,
#         "duration" : duration}
##---------------------------------------------##

##------------------ Part 12 ------------------##
from fastapi import Cookie, Header
from typing import List

@app.get("/items")
async def read_items(
    cookie_id : Optional[str] = Cookie(None),
    accept_encoding : Optional[str] = Header(None),
    sec_ch_ua : Optional[str] = Header(None),
    user_agent : Optional[str] = Header(None),
    x_token : list[str] = Header(None),                # 활성화
    # x_token : Optional[List[str]] = Header(None),    # 비활성화
    # x_token : List = Header(None)                    # 활성화
    ):

    return {
        "cookie_id" : cookie_id,
        "Accept-Encoding" : accept_encoding,
        "sec-ch-ua" : sec_ch_ua,
        "User-Agent" : user_agent,
        "X-Token values" : x_token,
    }
##---------------------------------------------##