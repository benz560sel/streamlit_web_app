import streamlit as st
import pandas as pd



df = pd.read_csv('./data/平均気温.csv', index_col='月')
st.line_chart(df)
st.bar_chart(df)

