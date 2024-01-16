# 기존에 존재하는 database를 sqlalchemy를 이용해 연결해주는 파일

from sqlalchemy import *
from sqlalchemy.orm import sessionmaker # 한번 접속되면 로그인을 유지해주는 역할을 하는 라이브러리

# DB_URL = 'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}'
DB_URL = 'mysql+pymysql://root:apptools@127.0.0.1:3306/flyai'
# 원래는 user를 추가해서 해야하는데 지금은 시간 관계상 root를 하는 것
# user를 추가해서 r, w, x에 대한 권한을 설정하고 접속해야 한다
# fastapi는 이처럼 DB의 username과 password가 보이기 때문에 해킹 되면 DB까지 털린다고 봐야 한다

# 데이터 베이스를 접속하기 위해 만드는 클래스
# 빈번하게 접속하는 경우를 위해 클래스화 해놓은 것
class engineconn: 
    def __init__(self):
        self.engine = create_engine(DB_URL, pool_recycle = 500)

    def sessionmaker(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        return session

    def connection(self):
        conn = self.engine.connect() # 실질적으로 접속하는 부분
        return conn