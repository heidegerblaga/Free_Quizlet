from random import randint
from model import (Base, session,
                    Lern, engine)
import os
import numpy as np
import pandas as pd
import math
import streamlit as st
from Word import Word


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


    with open('set.txt','w+',encoding='utf-8') as file:

        for i in range(0,len(set)-1):

            file.write(f'{set[i].polish} # {set[i].infinitive} {set[i].simple_past} {set[i].past_participle} {set[i].point}\n')










class Quiz():

    def __init__(self,dic):


            set = []


            with open('set.txt','r+',encoding='utf-8') as file:

                for line in file.readlines():




                    line = line.split('#')
                    print(line[1].split())
                    set.append(Word(polish=line[0],infinitive=line[1].split()[0],
                                    simple_past=line[1].split()[1],past_participle=line[1].split()[1],point=int(line[1].split()[3])))


            st.title('QUIZ')
            if 'i' not in st.session_state:
                st.session_state.i = 0

            answers = []




           # st.text(f'\nPytanie nr.{int(st.session_state.i) + 1}')


            with st.form(f'form_{st.session_state.i}'):
                    st.text(set[st.session_state.i].polish)
                    ans_infinitive = st.text_input('infinitive', key=f'infinitive_input_{st.session_state.i}')
                    ans_simple_past = st.text_input('simple_past', key=f'simple_past_input_{st.session_state.i}')
                    ans_past_participle = st.text_input('past_participle', key=f'past_participle_input_{st.session_state.i}')
                    submit_button = st.form_submit_button(label='Zatwierdź odpowiedź')

            if submit_button:

                st.write(f'to  {ans_infinitive} - {ans_simple_past} - {ans_past_participle} ')


                if ((ans_infinitive==set[st.session_state.i].infinitive)and
                            (ans_simple_past==set[st.session_state.i].simple_past)and
                            (ans_past_participle==set[st.session_state.i].past_participle)):

                        st.text('To poprawna odpowiedz ! trzymaj tak dalej ! :)')
                        set[st.session_state.i].add_point()
                        addpoint=session.query(Lern).filter(Lern.infinitive==set[st.session_state.i].infinitive).first()
                        addpoint.point = set[st.session_state.i].point
                        session.add(addpoint)
                        st.text(set[st.session_state.i].point)
                        session.commit()
                        st.session_state.i += 1




                else:
                        st.text(f'Blad ! poprawna odpowiedz : {set[st.session_state.i].infinitive} - {set[st.session_state.i].simple_past} - {set[st.session_state.i].past_participle}')
                        set[st.session_state.i].subtract_point()
                        addpoint = session.query(Lern).filter(Lern.infinitive == set[st.session_state.i].infinitive).first()
                        addpoint.point = set[st.session_state.i].point
                        session.add(addpoint)
                        st.text(set[st.session_state.i].point)
                        session.commit()
                        st.session_state.i += 1




            st.write('Count = ', st.session_state.i)













