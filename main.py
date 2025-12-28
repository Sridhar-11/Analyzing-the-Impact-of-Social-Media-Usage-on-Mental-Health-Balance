import streamlit as st
import pandas as pd
st.title("Wellcome to Sridhar Methuku profile")


file= st.file_uploader("uploead",type="csv")
if file:
    st.write(pd.read_csv(file))


