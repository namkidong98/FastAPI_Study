from fastapi import FastAPI
from pydantic import BaseModel

from database import engineconn # database.py의 engineconn 클래스를 불러오는 것
from models import Chatbot      # models.py의 chatbot 클래스를 불러오는 것

app = FastAPI()
engine = engineconn() # DB에 접속한 정보를 담은 engine
session = engine.sessionmaker() # engine에서 connect해서 나온 session값을 session 변수에 저장
                                # 필요할 때, 그때그때 사용할 예정

@app.get("/chatbot")
async def first_get():
    example = session.query(Chatbot).all() # all로 해당하는 모든 행을 가져와서 리턴
    return example