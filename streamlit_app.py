import streamlit as st
import pandas as pd

st.title("UFO Sightings")
st.header("Introduction")
st.write("UFO's always seem to be reported, today you will find out how often it really is. This is a dashboard that shows")
st.write("everything about UFO's and when they are seen.")
df = pd.read_csv("ufo.csv")
df1 = df
df2 = df
df3 = df
df4 = df


st.write(df.head(10))

st.header("Sightings of UFO's by Country")

st.write("Below is a Bar graph and Pie chart representing how many sightings are reported on UFO's")

top_5_states =df['Country'].value_counts().head(5)
top_5_states.plot.bar()



