from random import randint
from model import (Base, session,
                    Lern, engine)
import os
import numpy as np
import pandas as pd
import math







def session_set(dic):

    set = []
    pnt = []

    for i in range(0, len(dic) - 1):
        pnt.append(dic[i].point)


    while len(set)<20:
       for i in range(0,len(dic)-1):
        normalVar = math.floor(np.random.normal(min(pnt)+1, 5, 1) / 2)

        if ((dic[i].point==normalVar)and(dic[i] not in set)and(len(set)<20)):
            set.append(dic[i])


    return set




class Quiz():

    def __init__(self,dic):

        cnt = True
        while cnt:
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
                    session.add(addpoint)
                    print(set[i].point)
                    session.commit()


                    input()

                else:
                    print(f'Blad ! poprawna odpowiedz : {set[i].infinitive} - {set[i].simple_past} - {set[i].past_participle}')
                    set[i].subtract_point()
                    addpoint = session.query(Lern).filter(Lern.infinitive == set[i].infinitive).first()
                    addpoint.point = set[i].point
                    session.add(addpoint)
                    print(set[i].point)
                    session.commit()
                    input()





            print('''\nJeszcze jedna sesja ?
                        \r1.Tak
                        \r2.Nie''')
            choice = input()
            if choice == 2:

               break

            cnt=False






