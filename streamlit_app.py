import streamlit as st
import pandas as pd

st.title("Streamlit on Replit")


df = pd.read_csv("ufo.csv")

st.write(df.head(1))