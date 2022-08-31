import streamlit as st
from PIL import Image
import pandas as pd



st.title('Study Python')
st.caption('Python_学習用アプリ')

image = Image.open('./data/porshe911.png')
st.image(image)
