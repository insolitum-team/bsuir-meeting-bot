from sqlalchemy import Text, Column, Integer, BigInteger, String, sql

from bot.database.main import TimedBaseModel


class User(TimedBaseModel):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    user_id = Column(BigInteger)
    username = Column(String(50))
    status = Column(String(30))
    gender = Column(String(30))
    name = Column(String(50))
    native_city = Column(String(40))
    age = Column(Integer)
    faculty = Column(String(60))
    speciality = Column(String(256))
    university_year = Column(Integer)
    description = Column(Text)
    photo_id = Column(String)

    query: sql.select
