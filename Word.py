# -*- coding: utf-8 -*-

class Word():



    def add_point(self):
        self.point=self.point+1

    def subtract_point(self):
        self.point=self.point-1


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








