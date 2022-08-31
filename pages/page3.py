import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('./data/平均気温.csv', index_col='月')
# st.dataframe(df)
# st.table(df)
st.line_chart(df)
st.bar_chart(df)
#matplotlibでグラフを作成
# fig,ax = plt.subplots()
# ax.plot(df.index)
# ax.set_title('matplotlib_graph')
# st.pyplot(fig)
