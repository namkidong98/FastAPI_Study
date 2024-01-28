from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from domain.question import question_router # ./domain/question/question_router.py를 포함
from domain.answer import answer_router     # ./domain/answer/answer_router.py를 포함

app = FastAPI()

origins = [
    'http://127.0.0.1:5173',
    'http://localhost:5173',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
) 

app.include_router(question_router.router) # question_router 파일의 router 객체를 포함
app.include_router(answer_router.router)   # answer_router 파일의 router 객체를 포함

# 맨 처음 테스트를 위해 사용
# @app.get("/hello")
# def hello():
#     return {"message" : "안녕하세요 파이보!"}