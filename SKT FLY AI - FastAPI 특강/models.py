# database.py에서 연결한 db를 테이블과 매핑시키는 역할
# 이 파일이 custom해서 사용할 부분

from sqlalchemy import Column, TEXT, INT, BIGINT
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

# Query와 동일한 개념을 풀어 쓴 것이라고 생각하면 된다
class Chatbot(Base): 
    __tablename__ = "chatbot"
    num = Column(BIGINT, nullable=False, autoincrement=True, primary_key=True)
    type = Column(TEXT, nullable=False)
    msg = Column(TEXT, nullable=False)