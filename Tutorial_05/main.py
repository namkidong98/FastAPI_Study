from fastapi import FastAPI, Query, Path, Body
from pydantic import BaseModel, Field, HttpUrl
from typing import Optional

app = FastAPI()

##------------------ Part 13 ------------------##
# from pydantic import EmailStr
# from typing import Literal

# class UserBase(BaseModel):
#     username : str
#     #password : str  # password가 그대로 노출되면 안 되기 때문에 조치가 필요
#     email : EmailStr
#     full_name : Optional[str] = None

# class UserIn(UserBase):
#     password : str

# class UserOut(UserBase):
#     pass

# @app.post("/user/", response_model= UserOut)
# async def create_user(user: UserIn):
#     return user



# class Item(BaseModel):
#     name : str
#     description : Optional[str] = None
#     price : float
#     tax : Optional[float] = None
#     tags : list[str] = []

# items = {
#     "foo" : {"name" : "Foo", "price" : 50.2},
#     "bar" : {"name" : "Bar", "description" : "The bartenders", "price" : 2, "tax" : 20.2},
#     "baz" : {"name" : "Baz", "description" : None, "price" : 50.2, "tax" : 10.5, "tags" : []}
# }

# @app.get("/items/", response_model=Item, response_model_exclude_unset=True)
# async def read_item(item_id : Literal["foo", "bar", "baz"]):
#     return items[item_id]

# @app.post("/items/", response_model=Item)
# async def create_item(item : Item):
#     return item

# @app.get("/items/{item_id}/name", response_model=Item, response_model_include={"name", "description"})
# async def read_item_name(item_id : Literal["foo", "bar", "baz"]):
#     return items[item_id]

# @app.get("/items/{item_id}/public", response_model=Item, response_model_exclude={"tax"})
# async def read_items_public_data(item_id : Literal["foo", "bar", "baz"]):
#     return items[item_id]
##---------------------------------------------##



##------------------ Part 14 ------------------##
from pydantic import EmailStr
from typing import Literal

class UserBase(BaseModel):
    username : str
    email : EmailStr
    full_name : Optional[str] = None

class UserIn(UserBase):
    password : str

class UserOut(UserBase):
    pass

class UserInDB(UserBase):
    hashed_password : str

def fake_password_hasher(raw_password : str):
    return f"supersecret{raw_password}"

def fake_save_user(user_in : UserIn):
    hashed_password = fake_password_hasher(user_in.password)

    # model_dump() : 사용자 입력을 딕셔너리로 변환
    # ** : unpacking, 딕셔너리의 내용을 key:value들의 나열로 풀어서 전달
    user_in_db = UserInDB(**user_in.model_dump(), hashed_password=hashed_password)
    print("User 'saved'.")
    return user_in_db

@app.post("/user/", response_model=UserOut)
async def create_user(user_in : UserIn):
    user_saved = fake_save_user(user_in)
    print(user_saved)
    return user_saved

from typing import Union

class BaseItem(BaseModel):
    description : str
    type : str

class CarItem(BaseItem):
    type : str = "car"

class PlaneItem(BaseItem):
    type : str = "plane"
    size : int
    

items = {
    "item1" : {"description" : "All my friends drive a low rider", "type" : "car"},
    "item2" : {"description" : "Music is my aeroplane, it's my aeroplane",
               "type" : "plane",
               "size" : 5}
}

@ app.get("/item/{item_id}/", response_model=Union[PlaneItem, CarItem])
async def read_item(item_id : Literal["item1", "item2"]):
    return items[item_id]
##---------------------------------------------##