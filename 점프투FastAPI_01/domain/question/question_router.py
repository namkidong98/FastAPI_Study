from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
# from database import SessionLocal # get_db로 인해 불필요해짐

from domain.question import question_schema, question_crud 
# from models import Question # question_crud로 인해 불필요해짐
from starlette import status

router = APIRouter( # APIRouter 클래스로 생성한 router 객체
    prefix = "/api/question",   # prefix : 요청 URL 앞부분에 항상 포함되어야 하는 값
)

# /api/question/list라는 URL 요청에 대응(prefix 때문)
@router.get("/list", response_model=list[question_schema.Question]) # 리턴값은 Question 스키마로 구성된 리스트    
def question_list(db : Session = Depends(get_db)):  # Session과 Depends를 사용해서 의존성을 추가할 수 있다
    _question_list = question_crud.get_question_list(db) # CRUD 부분은 따로 분리하였다
    return _question_list

@router.get("/detail/{question_id}", response_model=question_schema.Question)   # 리턴은 하나의 Question 객체
def question_detail(question_id : int, db : Session = Depends(get_db)): # path parameter 'question_id' 받음
    question = question_crud.get_question(db, question_id) # crud.py에서 정의한 함수로 해당 question_id로
    return question                                                      # Question 객체를 조회해서 반환

@router.post("/create", status_code=status.HTTP_204_NO_CONTENT)         # 질문 등록 API에는 리턴할 응답이 없으므로
def question_create(_question_create:question_schema.QuestionCreate,    # # 라우터 함수의 응답으로 response_model 대신 status_code를 사용한다
                    db : Session = Depends(get_db)):
    question_crud.create_question(db = db, question_create = _question_create)