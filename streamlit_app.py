import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

st.title("UFO Sightings")
st.header("Introduction")
st.write(
  "UFO's always seem to be reported, today you will find out how often it really is. This is a dashboard that shows everything about UFO's and when they are seen."
)
df = pd.read_csv("ufo.csv")
df1 = df
df2 = df
df3 = df
df4 = df

st.write(df.head(10))

st.header("Sightings of UFO's by Country")

st.subheader(
  "Below is a Bar graph and Pie chart representing how many sightings are reported on UFO's by Countries around the world"
)

top_5_states = df['Country'].value_counts().head(5)
st.bar_chart(top_5_states)

top_5_states = df['Country'].value_counts().head(3)

st.plotly_chart(
  px.pie(top_5_states,
         values=top_5_states.values,
         names=top_5_states.index,
         title='Top 3 Countries with UFO Sightings'))

st.write(
  "The above data shows that the US has far more UFO sightings than either the UK or Canada combined"
)

st.header("Sightings of UFO's by US States and Cities")

st.subheader(
  "Now we'll look at how US sightings of UFO's are spread out amoung states and cities"
)

top_5_states = df['State'].value_counts().head(5)

st.plotly_chart(
  px.pie(top_5_states,
         values=top_5_states.values,
         names=top_5_states.index,
         title='Top 5 US States with UFO Sightings'))

st.write(
  "The Data of UFO Reports by State shows that California has the most sightings with Florida in Second and Texas in Third"
)

top_5_states = df['City'].value_counts().head(5)

st.plotly_chart(
  px.pie(top_5_states,
         values=top_5_states.values,
         names=top_5_states.index,
         title='Top 5 US Cities with UFO Sightings'))

st.write(
  "The Data of UFO Reports by City shows that Tucson has the most sightings with 13 Reports while Portland and Seattle have 11 and 10 Reports respectively"
)

st.header("Hypothesis #3:")
st.subheader("What can we tell about the duration of UFO Sightings")

st.title('Histogram of Duration')
plt.hist(df2["Duration"], range=[0, 100])
st.pyplot()

#Sets the title of the graph
plt.title("Histogram: Duration of UFO Sightings")
st.write(
  "Looking at this histogram we can tell that the majority of reported UFO sightings last between 0 and 10 seconds"
)

st.header("Hypothesis #4:")
st.subheader(
  "Does the observed shape of the UFO have any relation to how long the sightings lasts?"
)
# Apply the default theme
sns.set_theme()
df22 = df2[(df2['Shape'].isin(["Circle", "Light", "Triangle", "Orb"]))
           & (df2['Duration'] < 30) & (df2['Duration'] > 10)]
#Creaes the Box Plot.

st.title('Histogram: UFO Sighting Duration Compared to Shape')
sns.histplot(df22, x='Shape', hue='Duration')
plt.xlabel('Shape')
plt.ylabel('Frequency')
plt.title('Histogram: UFO Sighting Duration Compared to Shape')
st.pyplot()


st.write(
  "Looking at this box plot we can see that the observed shape of the UFO is independent of the length of the sighting"
)

st.header("Hypothesis #5:")
st.subheader("What are the most common shapes of UFO's?")

top_10_states = df['Shape'].value_counts().head(5)

st.title("Area Chart: Shapes of UFO's")
st.plotly_chart(px.area(top_10_states, values='top_10_states', names=top_10_states.index, title="Shapes of UFO's"))

top_10_states = df['Shape'].value_counts().head(20)
st.plotly_chart(
  px.pie(top_10_states,
         values='top_10_states',
         names='top_10_states.index',
         title="Shapes of UFO's"))
st.write(
  "These graphs show the most common shapes of UFO's are light, circle, and triangle."
)

st.header("Hypothesis #6:")
st.subheader("Does the country have anything to do with the shape of the UFO?")

USA = df[df["Country"] == "USA"].head(20)
df = df[df['Shape'] != 'Unknown']

top_10_states = USA['Shape'].value_counts().head(20)
st.plotly_chart(
  px.bar(top_10_states,
         values='top_10_states',
         names='top_10_states.index',
         title="Shape's of UFO's in the USA"))

UK = df[df["Country"] == "United Kingdom"].head(20)
df = df[df['Shape'] != 'Unknown']

top_10_states = UK['Shape'].value_counts().head(20)
st.plotly_chart(
  px.bar(top_10_states,
         values='top_10_states',
         names='top_10_states.index',
         title="Shape's of UFO's in the UK"))

CAN = df[df["Country"] == "Canada"].head(20)
df = df[df['Shape'] != 'Unknown']

top_10_states = CAN['Shape'].value_counts().head(20)
st.plotly_chart(
  px.bar(top_10_states,
         values='top_10_states',
         names='top_10_states.index',
         title="Shape's of UFO's in Canada"))

AUS = df[df["Country"] == "Australia"].head(20)

top_10_states = AUS['Shape'].value_counts().head(20)
st.plotly_chart(
  px.bar(top_10_states,
         values='top_10_states',
         names='top_10_states.index',
         title="Shape's of UFO's in Australia"))

st.write(
  "These graphs show that in different countries both light and circle are towards the top of the most common but the order of the other shapes is very different. Therefore to an extent where you live matters for the shapes of UFO's you will see."
)
