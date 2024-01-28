from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import contextlib

SQLALCHEMY_DATABASE_URL = "sqlite:///./myapi.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args = {"check_same_thread" : False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# autocommit이 True이면 commit 없이 즉시 데이터베이스에 변경사항이 적용된다
# 따라서 rollback도 불가능하기 때문에 autocommit을 False로 설정하는 것이 안전하다

Base = declarative_base()

#@contextlib.contextmanager # with구문 대신 db:Session=Depend를 사용하면
                            # 자동으로 contextmanager가 적용되기 때문에 이 부분을 제거해줘야 한다 
def get_db():           # Generator 함수
    db = SessionLocal() # db 세션 객체
    try:
        yield db    # db 세션 객체를 리턴
    finally:        # db세션 객체를 사용한 작업이 마무리되면 finally가 실행
        db.close()  # 자동적으로 db.close()를 수행