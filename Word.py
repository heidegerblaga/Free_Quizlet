# -*- coding: utf-8 -*-

class Word():


    def add_point(self):

      if(self.point<5):
        self.point=self.point+1



    def subtract_point(self):
       if (self.point > -5):
        self.point=self.point-1


    def __init__(self,polish,infinitive,simple_past,past_participle,point):
        self.polish = polish
        self.infinitive = infinitive
        self.simple_past = simple_past
        self.past_participle = past_participle
        self.point = point


    def __repr__(self):
        return f'''\nsłowo : {self.polish}
         \rinfinitive : to {self.infinitive}
         \rsimple past : {self.simple_past}
          \rpast participle : {self.past_participle}'''








