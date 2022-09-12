from sqlalchemy import (create_engine,Column,
                        Integer,String,Date,update)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from Word import Word



engine = create_engine('sqlite:///learning.db',echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()



class Lern(Base):

    __tablename__='learning'

    id = Column(Integer, primary_key=True)
    polish = Column('Polish', String)
    infinitive = Column('Infinitive', String)
    simple_past = Column('Simple past', String)
    past_participle = Column('Past participle', String)
    point = Column('Knowlege', Integer)


if __name__ == '__main__':
    Base.metadata.create_all(engine)


dic=[]

for i in range(77,102):

    stmt = (
        update(Lern).
            where(Lern.id == i).
            values(Knowlege=0)
    )

session.commit()

for word in session.query(Lern):

    dic.append(Word(word.polish, word.infinitive, word.simple_past, word.past_participle, word.point))


