from datetime import datetime, date, time
import streamlit as st
import plotly.express as px

st.markdown("## サプライ・チェイン最適化チャンネル（MIKIO KUBO)の内容実践結果")
st.markdown("# Streamlit Demo")
code = '''
mport streamlit as st
st.title('Study Python')

'''

st.code(code, language='Python')

st.markdown("## マークダウンで書くことができる。　$x^2$")
code1='''
st.markdown("## マークダウンで書くことができる。　$x^2$")
'''
st.code(code1, language='Python')
st.markdown("## アイリスデータの表示")
st.markdown("ガクの長さ　　,ガクの幅　　,花弁の長さ　　,花弁の幅　　")
df = px.data.iris()

df
code2='''
df = px.data.iris()

df
'''
st.code(code2, language='Python')
st.write("散布図")
st.write(px.scatter(df,x="sepal_length",y="sepal_width",color="species"))
code3='''
st.write(px.scatter(df,x="sepal_length",y="sepal_width",color="species"))
'''
st.code(code3, language='Python')

if st.button('Say hello'):
    st.write('こんにちは')
else:
    st.write('Goodbye')

code4='''
if st.button('Say hello'):
    st.write('こんにちは')
else:
    st.write('Goodbye')
'''
st.code(code4, language='Python')
st.write('上から実行されるので一度押されるとそれ以外は認識されない欠点がある')

agree = st.checkbox('チェックして下さい')
if agree:
    st.write('Great')

code5='''
agree = st.checkbox('チェックして下さい')
if agree:
    st.write('Great')
'''
st.code(code5, language='Python')

fruit=st.radio(label="好きなフルーツは?",options=["バナナ","りんご","いちご"],index=1)
st.write(fruit)
code6='''
fruit=st.radio(label="好きなフルーツは?",options=["バナナ","りんご","いちご"],index=1)
st.write(fruit)
'''
st.code(code6, language='Python')

option = st.selectbox('今日は何をする?',('なわとび','野球','ゲーム'))
st.write('よし　',option,"をしよう!")
code7='''
option = st.selectbox('今日は何をする?',('なわとび','野球','ゲーム'))
st.write('よし　',option,"をしよう!")
'''
st.code(code7, language='Python')

options = st.multiselect('何色が好きですか？', options=[
                         'Green', 'Yellow', 'Red', 'Blue'], default=['Yellow', 'Red'])
st.write('You selected: ',options)
code8='''
options = st.multiselect('何色が好きですか？', options=[
                         'Green', 'Yellow', 'Red', 'Blue'], default=['Yellow', 'Red'])
st.write('You selected: ',options)
'''
st.code(code8, language='Python')

age = st.slider('何歳？',min_value=0,max_value=100,value=25)
st.write(age)

code9='''
age = st.slider('何歳？',min_value=0,max_value=100,value=25)
st.write(age)
'''
st.code(code9, language='Python')

interval = st.slider("計画時間は？",value=(datetime(2023,1,1,12,31),datetime(2024,1,1,12,31)),format="MM/DD/YY -hh:mm")
code10='''
interval = st.slider("計画時間は？",value=(datetime(2023,1,1,12,31),datetime(2024,1,1,12,31)),format="MM/DD/YY -hh:mm")
'''
st.code(code10, language='Python')

color = st.select_slider('色を選んで下さい',options=['red','yellow','orange','green','blue','indigo','violet'])
st.write(color)

code11 = '''
color = st.select_slider('色を選んで下さい',options=['red','yellow','orange','green','blue','indigo','violet'])
st.write(color)
'''
st.code(code11, language='Python')

title = st.text_input('名前を入れて下さい',value='氏名')
st.write(title)

number = st.number_input('数値を入力してください',
                         min_value=1.0,max_value=10.0,value=5.0,step=0.1)
st.write(number)
code12 = '''
number = st.number_input('数値を入力してください',
                         min_value=1.0,max_value=10.0,value=5.0,step=0.1)
'''
st.code(code12, language='Python')

d = st.date_input("誕生日は？",date(2022,10,1))

alarm = st.time_input('アラームセット',time(8,45))