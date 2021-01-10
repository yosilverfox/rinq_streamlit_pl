import streamlit as st
import pandas as pd

st.title('RINQWARE 決算公告')
"損益計算書(P/L)"
pl_df = pd.read_csv('csv/pl.csv', index_col=0)

options = st.multiselect(
    "表示する項目を選択してください。",
    list(pl_df.columns),
    default=list(pl_df.columns),
    )

if options:
   st.line_chart(pl_df[options])
   pl_df = pl_df.applymap('{:,}'.format) 
   st.table(pl_df)