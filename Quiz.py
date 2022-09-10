from random import randint
from model import (Base, session,
                    Lern, engine)
import os



def session_set(dic):
    well= []
    lern = []
    non =[]
    set = []

    for i in range(0,len(dic)-1):

        if dic[i].point>=5:
           well.append(dic[i])
        elif ((dic[i].point<5)and(dic[i].point>=1)):
            lern.append(dic[i])

        elif dic[i].point < 1:
                non.append(dic[i])

    i=0
    while i!=20:



        while i!=2:

            duplic = True
            j = lern[randint(0, len(lern) - 1)]
            if (j not in set):
                set.append(j)
                i += 1

                duplic = False




        while i!=15:

            duplic = True
            while duplic:
                j = lern[randint(0, len(lern) - 1)]
                if (j not in set):
                   set.append(j)
                   i += 1

                   duplic = False

        while i != 20:
            duplic = True
            while duplic:
                j = non[randint(0, len(non) - 1)]
                if (j not in set):
                    set.append(j)
                    i += 1
                    duplic = False



    return set




class Quiz():

    def __init__(self,dic):

        cnt = True
        while cnt:
            set = session_set(dic)
            for i in range(0,len(set)):

                j = randint(0,len(set)-1)

                print(f'\nPytanie nr.{i+1}')
                ans_infinitive =''
                ans_simple_past =''
                ans_past_participle =''

                print(f'\r{set[j].polish} -  ')


                ans_infinitive=input()
                ans_simple_past=input()
                ans_past_participle=input()

                print(f'to {ans_infinitive} - {ans_simple_past} - {ans_past_participle} ')

                if ((ans_infinitive==set[j].infinitive)and
                        (ans_simple_past==set[j].simple_past)and
                        (ans_past_participle==set[j].past_participle)):
                    print('To poprawna odpowiedz ! trzymaj tak dalej ! :)')
                    set[i].add_point()
                    addpoint=session.query(Lern).filter(Lern.infinitive==set[j].infinitive).first()
                    addpoint.point = set[j].point
                    session.add(addpoint)
                    print(set[j].point)
                    session.commit()


                    input()

                else:
                    print(f'Blad ! poprawna odpowiedz : {set[j].infinitive} - {set[j].simple_past} - {set[j].past_participle}')
                    set[j].subtract_point()
                    addpoint = session.query(Lern).filter(Lern.infinitive == set[j].infinitive).first()
                    addpoint.point = set[j].point
                    session.add(addpoint)
                    print(set[j].point)
                    session.commit()
                    input()





            print('''\nJeszcze jedna sesja ?
                        \r1.Tak
                        \r2.Nie''')
            choice = input()
            if choice == 2:
             cnt = False






