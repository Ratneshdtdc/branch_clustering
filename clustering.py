import streamlit as st

st.title(':blue[Branch Clustering Model]')

option = st.selectbox(
   "Select Branch Name/Code.",
   ("Email", "Home phone", "Mobile phone"),
   index=None,
   placeholder="Select Branch Name/Code...",
)

st.write('You selected:', option)

