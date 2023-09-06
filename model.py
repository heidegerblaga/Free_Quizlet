from sqlalchemy import (create_engine,Column,
                        Integer,String,Date,update)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from Word import Word
from psql import engine



Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

dbConnection = engine.connect()


class Lern(Base):

    __tablename__='learning'

    id = Column(Integer, primary_key=True)
    polish = Column('Polish', String)
    infinitive = Column('Infinitive', String)
    simple_past = Column('Simple past', String)
    past_participle = Column('Past participle', String)
    point = Column('Knowlege', Integer)

class Progres(Base):

    __tablename__='progres'

    id = Column(Integer, primary_key=True)
    count = Column('count', Integer)



if __name__ == '__main__':
    Base.metadata.create_all(engine)


dic=[]



session.commit()

for word in session.query(Lern):

    dic.append(Word(word.polish, word.infinitive, word.simple_past, word.past_participle, word.point))
