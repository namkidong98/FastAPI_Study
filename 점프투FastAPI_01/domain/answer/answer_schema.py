import datetime
from pydantic import BaseModel, field_validator

class AnswerCreate(BaseModel):  # 답변 등록시 사용할 스키마
    content : str               # 답변 등록에 전달되는 유일한 파라미터, 유일하기에 필수값(nullable=False)

    @field_validator('content')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError("빈 값은 허용하지 않습니다.")
        return v

class Answer(BaseModel):    # Answer 스키마는 출력으로 사용할 답변 1건을 의미
    id : int
    content : str
    create_date : datetime.datetime