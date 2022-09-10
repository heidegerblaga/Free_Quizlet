from random import randint
from model import (Base, session,
                    Lern, engine)


def session_set(dic):

    set = []
    for i in range(0,20):
        set.append(dic[randint(0,len(dic)-1)])

    return set




class Quiz():

    def __init__(self,dic):
        set=session_set(dic)
        while True:

            for i in range(0,len(set)):

                print(f'\nPytanie nr.{i+1}')
                ans_infinitive =''
                ans_simple_past =''
                ans_past_participle =''
                j = randint(0,len(set)-1)
                print(f'\r{set[j].polish} -  ')


                ans_infinitive=input()
                ans_simple_past=input()
                ans_past_participle=input()

                print(f'to {ans_infinitive} - {ans_simple_past} - {ans_past_participle} ')

                if ((ans_infinitive==set[j].infinitive)and
                        (ans_simple_past==set[j].simple_past)and
                        (ans_past_participle==set[j].past_participle)):
                    print('To poprawna odpowiedz ! trzymaj tak dalej ! :)')
                    set[j].add_point()
                    addpoint=session.query(Lern).filter(Lern.infinitive==set[j].infinitive).first()
                    addpoint.point = set[j].point
                    print(set[j].point)
                    session.commit()

                    input()

                else:
                    print(f'Blad ! poprawna odpowiedz : {set[j].infinitive} - {set[j].simple_past} - {set[j].past_participle}')
                    set[i].subtract_point()
                    addpoint = session.query(Lern).filter(Lern.infinitive == set[j].infinitive).first()
                    addpoint.point = set[j].point
                    print(set[j].point)
                    session.commit()
                    input()



            print('''\nJeszcze jedna sesja ?
            \r1.Tak
            \r2.Nie''')
            choice = input()
            if choice == 1:
               pass
            else:
                return None





