import pandas as pd
import streamlit as st
import psycopg2
import matplotlib.pyplot as plt


conn = psycopg2.connect(user="postgres",
              password="qwest1",
              host="localhost",
              database="english")


query = "SELECT * FROM learning"

df = pd.read_sql(query,conn)


query = "SELECT * FROM progres"

progres = pd.read_sql(query,conn)

chart_data1 = progres['count']


st.title('Count of good answers per session')
st.line_chart(chart_data1)




chart_data = df

st.markdown('\n \n \n \n \n \n \n \n')

st.title('Knowledge level of particular words')


st.bar_chart(
    chart_data,
    x='Infinitive',
    y='Knowlege',
    width=100
)

st.title('Most common mistakes')

st.dataframe( df.sort_values(by='Knowlege', ascending=True).head(10))
