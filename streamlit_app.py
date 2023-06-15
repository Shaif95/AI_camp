import streamlit as st
import pandas as pd
import plotly.express as px

st.title("UFO Sightings")
st.header("Introduction")
st.write("UFO's always seem to be reported, today you will find out how often it really is. This is a dashboard that shows everything about UFO's and when they are seen.")
df = pd.read_csv("ufo.csv")
df1 = df
df2 = df
df3 = df
df4 = df


st.write(df.head(10))

st.header("Sightings of UFO's by Country")

st.write("Below is a Bar graph and Pie chart representing how many sightings are reported on UFO's by Countries around the world")

top_5_states =df['Country'].value_counts().head(5)
st.bar_chart(top_5_states)

top_5_states = df['Country'].value_counts().head(3)








st.header("Hypothesis #3:")
st.subheader("What can we tell about the duration of UFO Sightings")
#Creates the histogram with the correct range
plt.hist(df2["Duration"], range=[0, 100])
#Sets the title of the graph
plt.title('Histogram: Duration of UFO Sightings')
st.write("Looking at this histogram we can tell that the majority of reported UFO sightings last between 0 and 10 seconds")

st.header("Hypothesis#4")
st.subheader("Does ")

st.header("Hypothesis #4:")
st.subheader("What are the most common shapes of UFO's?")

top_10_states = df['Shape'].value_counts().head(5)
plt.fill_between(top_10_states.index, top_10_states.values)
plt.title("Shapes of UFO's")



st.header("Hypothesis #5:")
st.subheader("")





