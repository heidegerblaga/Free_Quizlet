# -*- coding: utf-8 -*-

from random import randint
from model import Lern




class Word():



    def add_point(self):
        self.point=+1

    def subtract_point(self):
        self.point=-1


    def __init__(self,polish,infinitive,simple_past,past_participle):
        self.polish = polish
        self.infinitive = infinitive
        self.simple_past = simple_past
        self.past_participle = past_participle
        self.point = 0

    def __repr__(self):
        return f'''\nsłowo : {self.polish}
         \rinfinitive : to {self.infinitive}
         \rsimple past : {self.simple_past}
          \rpast participle : {self.past_participle}'''

for i in range(0,len(dic)-2):
    base.append(Word(dic[i][0], dic[i][2], dic[i][4], dic[i][6]))
    #print(dic[i][2])

class Quiz():

    def __init__(self):

        while True:


            for i in range(0,len(base)-1):

                ans_infinitive =''
                ans_simple_past =''
                ans_past_participle =''
                j = randint(0,len(base)-1)
                print(f'{base[j].polish} -  ')


                ans_infinitive=input()
                ans_simple_past=input()
                ans_past_participle=input()

                print(f'to {ans_infinitive} - {ans_simple_past} - {ans_past_participle} ')

                if ((ans_infinitive==base[j].infinitive)and
                        (ans_simple_past==base[j].simple_past)and
                        (ans_past_participle==base[j].past_participle)):
                    print('To poprawna odpowiedz ! trzymaj tak dalej ! :)')
                    base[j].add_point()
                    input()

                else:
                    print(f'Blad ! poprawna odpowiedz : {base[j].infinitive} - {base[j].simple_past} - {base[j].past_participle}')
                    base[i].subtract_point()
                    input()



