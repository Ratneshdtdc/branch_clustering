import streamlit as st
import pandas as pd

st.title(':blue[Branch Clustering Model]')
df = pd.read_csv("")
branch_names = 

option = st.selectbox(
   "Select Branch Name/Code.",
   ("Email", "Home phone", "Mobile phone"),
   index=None,
   placeholder="Select Branch Name/Code...",
)

st.write('You selected:', option)

