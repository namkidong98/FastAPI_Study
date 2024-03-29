from models import Question
from sqlalchemy.orm import Session

from datetime import datetime
from domain.question.question_schema import QuestionCreate

def get_question_list(db : Session):
    question_list = db.query(Question).order_by(Question.create_date.desc()).all()
    return question_list

def get_question(db : Session, question_id : int):  # Path Parameter인 question_id를 받아서 
    question = db.query(Question).get(question_id)  # 해당 Question 객체를 반환
    return question

def create_question(db : Session, question_create: QuestionCreate):
    db_question = Question(subject = question_create.subject,
                           content = question_create.content,
                           create_date = datetime.now())
    db.add(db_question)
    db.commit()