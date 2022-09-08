from sqlalchemy import (create_engine,Column,
                        Integer,String,Date)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



engine = create_engine('sqlite:///learning.db')
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


word = session.query(Lern).filter(Lern.id == 66).first()
word.polish = 'opierac sie'
word.infinitive = 'leaned'
word.simple_past = 'leande'
word.past_participle = 'leande'


session.commit()