# -*- coding: utf-8 -*-

file = open("czasowniki.txt",'r+')

dic = []


for line in file.readlines():
    dic.append(line.split())


class Word():

    def __init__(self,polish,infinitive,simple_past,past_participle):
        self.polish = polish
        self.infinitive = infinitive
        self.simple_past = simple_past
        self.past_participle = past_participle

    def __repr__(self):
        return f'''\nsłowo : {self.polish}
         \rinfinitive : to {self.infinitive}
         \rsimple past : {self.simple_past}
          \rpast participle : {self.past_participle}'''


base = [ ]


for i in range(0,len(dic)-2):
    base.append(Word(dic[i][0], dic[i][2], dic[i][4], dic[i][6]))
    print(base[i])
    pass




class Quiz():
    def __init__(self,dictionary):
        self.dictionary = dictionary

    def quiz(self):
        live = 3
        i = 0
        answer = ''

        while live!=0:
            print(f'{self.dictionary[i]} - {input(answer)}')

















