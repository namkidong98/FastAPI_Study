from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from database import get_db
from domain.answer import answer_schema, answer_crud
from domain.question import question_crud

router = APIRouter(
    prefix = "/api/answer",
)

@router.post("/create/{question_id}", status_code=status.HTTP_204_NO_CONTENT)
def answer_create(question_id : int,    # path parameter인 question_id
                  _answer_create : answer_schema.AnswerCreate,
                  db : Session = Depends(get_db)):
    question = question_crud.get_question(db, question_id=question_id) # question_id로 Question 조회

    if not question: # 만약 해당하는 question이 없다면
        raise HTTPException(status_code=404, detail="Question not found") # '응답 없음'을 출력
    answer_crud.create_answer(db, question=question,    # question이 있으면 이에 대한
                              answer_create=_answer_create) # Answer 객체를 생성하고 db에 올린다(함수 내부적으로)
