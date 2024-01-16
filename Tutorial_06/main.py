from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

##------------------ Part 15 ------------------##
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
# 위의 사이트 주소에 각각의 status_code가 의미하는 바가 적혀있다
# 직접 status_code를 넣지 않고 fastapi의 status를 사용하면 직관적으로 확인할 수 있다

# from fastapi import status

# @app.post("/items/", status_code=201) # 201은 created
# async def create_item(name : str):
#     return {"name" : name}

# @app.delete("/items/{pk}", status_code=204) # 204는 No Content
# async def delete_item(pk : str):
#     print("pk", pk)
#     return pk

# @app.get("items", status_code=status.HTTP_301_MOVED_PERMANENTLY)
# async def read_items_redirect():
#     return {"hello" : "world"}
##---------------------------------------------##


##------------------ Part 16 ------------------##
# from fastapi import Form, Body

# @app.post("/login/")
# async def login(username : str = Form(...), password : str = Form(...)):
#     print("password", password)
#     return {"username" : username}

# @app.post("/login-json/")
# async def login_json(username : str = Body(...), password : str = Body(...)):
#     print("password", password)
#     return {"username" : username}
##---------------------------------------------##


##------------------ Part 17 ------------------##
# from fastapi import File, UploadFile
# from typing import Optional
# # Optional[bytes] = File(None) : Optional이 들어가는 경우 Docs에서 Upload 링크가 활성화되지 않는 문제가 발생한다
# # file : bytes | None = File(None) : 이러한 문법도 동일하게 오류가 발생한다 

# @app.post("/files/")
# async def create_file(file : bytes = File(None)):
#     if not file:
#         return {"message" : "No file sent"}
#     return {"file" : file}

# @app.post("/uploadfile/")
# async def create_upload_file(file : UploadFile = None):
#     if not file:
#         return {"message" : "No upload file sent"}
#     contents = await file.read()
#     print(contents)
#     return {"filename" : file.filename}

# @app.post("/list_files/")
# async def create_files(files : list[bytes] = File(..., description="A file read as bytes")):
#     return {"file_sizes" : [len(file) for file in files]}

# @app.post("/list_uploadfile/")
# async def create_upload_files(files : list[UploadFile] = File(..., description="A file read as UploadFile")):
#     return {"filenames" : [file.filename for file in files]}
##---------------------------------------------##

##------------------ Part 18 ------------------##
from fastapi import Form, File, UploadFile, Body

@app.post("/files/")
async def create_file(
    file : bytes = File(...),
    fileb : UploadFile = File(...),
    token : str = Form(...),
    hello : str = Body(...),
):
    return {
        "file_size" : len(file),
        "token" : token,
        "fileb_content_type" : fileb.content_type,
        "hello" : hello,
    }
##---------------------------------------------##