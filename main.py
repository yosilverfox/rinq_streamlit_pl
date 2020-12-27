import streamlit as st
import pandas as pd

st.title('RINQWARE 決算公告')
"損益計算書(P/L)"
pl = pd.read_csv('csv/pl.csv', index_col=0)
st.line_chart(pl)