import datetime

from pydantic import BaseModel, field_validator
from domain.answer.answer_schema import Answer

class Question(BaseModel): # BaseModel을 상속한 Question 객체 --> Question Schema
    id : int
    subject : str | None = None     # subject 값이 Null일 수 있음을 구현 --> nullable=True
    content : str
    create_date : datetime.datetime
    answers : list[Answer] = []     # Question 모델과 Answer 모델은 relationship으로 연결되어 있다
                                    # backref="answers"이므로 반드시 "answers"라는 이름의 속성으로 추가해야 한다

class QuestionCreate(BaseModel): # subject, content로 구성된 질문 등록 스키마
    subject : str
    content : str

    @field_validator('subject', 'content')  # subject와 content에는 빈 값을 허용하지 않는다
    def not_empty(cls, v):
        if not v or not v.strip():  # 만약 값이 없거나 빈 문자열이면
            raise ValueError("빈 값은 허용되지 않습니다.")  # ValueError를 일으킨다
        return v