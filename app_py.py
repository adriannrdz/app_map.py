import streamlit as st
import pandas as pd
#El pandas sirve para manipular las tabulaciones que tenemos en el Csv

df= pd.read_csv('https://raw.githubusercontent.com/adriannrdz/app_map.py/main/data.csv')

st.write(df)
st.map(df)
