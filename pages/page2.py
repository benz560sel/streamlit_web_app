import streamlit as st
from PIL import Image
import pandas as pd


with st.form(key = 'profile_form'):
    name = st.text_input('名前')
    address = st.text_input('住所')
    age_category = st.selectbox('年齢層',
                                ('子ども(18歳未満)', '大人（18歳以上）'))
    hobby = st.multiselect(
        '趣味',
        ('スポーツ観戦', '読書', 'プログラミング', 'アニメ・映画鑑賞', '釣り', '料理')
    )
    
    submit_btn = st.form_submit_button('送信')
    cancel_btn = st.form_submit_button('キャンセル')


    if submit_btn:
        st.text(f'ようこそ!{name}さん！{address}に書籍を送ります')
        st.text(f'年齢層：{age_category}')
        st.text(f'趣味：{",".join(hobby)}')
