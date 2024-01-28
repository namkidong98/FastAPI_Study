from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from database import Base

class Question(Base):
    __tablename__ = "question"

    id = Column(Integer, primary_key=True)  # primary_key로 중복값을 가질 수 없게 만듦
    subject = Column(String, nullable=True)
    content = Column(Text, nullable=False)  # Null값을 허용하지 않는다
    create_date = Column(DateTime, nullable=False)

class Answer(Base):
    __tablename__ = "answer"

    id = Column(Integer, primary_key=True)
    content = Column(String, nullable=False)
    create_date = Column(DateTime, nullable=False)
    question_id = Column(Integer, ForeignKey("question.id")) # question 테이블의 id 컬럼과 연결
    question = relationship("Question", backref="answers")   # 참조할 모델명과 역참조 설정