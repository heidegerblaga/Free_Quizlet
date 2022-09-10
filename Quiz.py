from random import randint
from model import (Base, session,
                    Lern, engine)
import os



def session_set(dic):

    set = []
    for i in range(0,20):

     duplic = True

     while duplic:

        j=dic[randint(0,len(dic)-1)]
        if (j not in set):
           set.append(j)
           duplic=False

        else:
           pass


    return set




class Quiz():

    def __init__(self,dic):

        while True:
            set = session_set(dic)
            for i in range(0,len(set)):

                print(f'\nPytanie nr.{i+1}')
                ans_infinitive =''
                ans_simple_past =''
                ans_past_participle =''

                print(f'\r{set[i].polish} -  ')


                ans_infinitive=input()
                ans_simple_past=input()
                ans_past_participle=input()

                print(f'to {ans_infinitive} - {ans_simple_past} - {ans_past_participle} ')

                if ((ans_infinitive==set[i].infinitive)and
                        (ans_simple_past==set[i].simple_past)and
                        (ans_past_participle==set[i].past_participle)):
                    print('To poprawna odpowiedz ! trzymaj tak dalej ! :)')
                    set[i].add_point()
                    addpoint=session.query(Lern).filter(Lern.infinitive==set[i].infinitive).first()
                    addpoint.point = set[i].point
                    print(set[i].point)
                    session.commit()


                    input()

                else:
                    print(f'Blad ! poprawna odpowiedz : {set[i].infinitive} - {set[i].simple_past} - {set[i].past_participle}')
                    set[i].subtract_point()
                    addpoint = session.query(Lern).filter(Lern.infinitive == set[i].infinitive).first()
                    addpoint.point = set[i].point
                    print(set[i].point)
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





