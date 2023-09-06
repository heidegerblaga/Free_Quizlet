from random import randint
from model import dic
from C_Quiz import Quiz , session_set
from model import (Base, session,
                    Lern, engine)


import streamlit as st

st.set_page_config(page_title='Quiz', page_icon='🏋', layout="centered", initial_sidebar_state="auto", menu_items=None)



Quiz(dic)