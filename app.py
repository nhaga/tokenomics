import streamlit as st
import pandas as pd
import numpy as np

st.sidebar.title('Thea Tokenomics')


st.sidebar.subheader('Offets')
offsets = st.sidebar.slider('Base Offset Amount in Protocol (mln tonnes)', 0, 1000, 100)
yearly_offsets = st.sidebar.slider('% increate in yearly offsets', 0, 20, 2)


st.sidebar.subheader('Actions')


actions = st.sidebar.slider('Base Actions Amount in Protocol (mln tonnes)', 0, 1000, 25)
yearly_actions = st.sidebar.slider('% increate in yearly actions', 0, 20, 2)

fee = st.sidebar.slider('Fee on actions (%)', 0, 10, 1)



years = range(2022, 2043)
df = pd.DataFrame({
    "Offsets": np.array([offsets * (1+yearly_offsets/100)**idx for idx, year in enumerate(years)]).cumsum(),
    "Actions": [actions * (1+yearly_actions/100)**idx for idx, year in enumerate(years)],
    "Fee": fee / 100 * actions
}, index=years)
df['fee_per'] = df['Fee'] / df['Offsets']

col1, col2 = st.columns(2)
with col1:
    st.table(data=df)


with col2:
    st.text('Fee Per Ton')
    st.line_chart(df['fee_per'])
