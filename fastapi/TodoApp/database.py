from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
# sqlalchemy: SQL toolkit mapper. 실제 DB에 사용되는 모델

SQLALCHEMY_DATABASE_URL = 'sqlite:///./todos.db'

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False}
)
# check_same_thread: True(default)일 경우 프로그래밍에러가 raised 됨. False이면 connection multiple thread로 접근되어 data corruption 방지

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# SessionLocal 클래스 생성. 이 클래스 객체는 데이터베이스의 세션 역할
# sessionmaker 이용하여 생성

Base = declarative_base()
# Base 클래스를 상속받아 데이터베이스의 모델 및 ORM 클래스 생성할 수 있음


