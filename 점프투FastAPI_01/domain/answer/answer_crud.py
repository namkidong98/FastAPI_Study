from datetime import datetime
from sqlalchemy.orm import Session
from domain.answer.answer_schema import AnswerCreate
from models import Answer, Question

# 답변을 등록하기 위한 create_answer 함수
# db와 Question 객체, AnswerCreate 객체를 받아서 모델 중 하나인 Answer 객체를 만들고 이를 db에 올린다
def create_answer(db : Session, question: Question, answer_create : AnswerCreate):
    db_answer = Answer(question = question,
                       content = answer_create.content,
                       create_date = datetime.now())
    db.add(db_answer)
    db.commit()