import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
import io

warnings.filterwarnings("ignore")
st.set_option('deprecation.showPyplotGlobalUse', False)

st.title("Protocol Parrots")

st.write(
  "My name is Derek, I am an Eight grader and I am learning to code so that I can code robots."
)
st.write(
  "My name is Carson, I am a junior and have recently learned how to code in Python"
)
st.write(
  "My name is Leighton, I'm a Sophmore and I'm learning Python from AI-camp so that I can learn how to code for Digital Art and Animation"
)

st.write(
  "My name is Toriaun, I am a freshman and I just learned how to code python")

st.title("UFO Sightings")
st.header("Introduction")
st.write(
  "UFO's always seem to be reported, today you will find out how often it really is. This is a dashboard that shows everything about UFO's and when they are seen. This presentation is based on some recent UFO reportings."
)
df = pd.read_csv("ufo.csv")
df1 = df
df2 = df
df3 = df
df4 = df

st.write(df.head(5))

st.header("Data Cleaning: Removing NaNs, Unknowns : ")

df = df[df['Shape'] != 'Unknown']
df["Images"] = df["Images"].apply(lambda x: "No" if x != "Yes" else x)

st.write(df.head(5))

st.header("Hypothesis #1 :")
st.subheader("Do the number of UFO sightings vary  across different countries?: Leighton")

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

st.header("Hypothesis #2:") 
          
st.subheader("The frequency of UFO sightings differs significantly among different states and cities within the United States: Leighton")

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
st.subheader("What can we tell about the duration of UFO Sightings?")

st.title('Histogram of Duration')
plt.hist(df2["Duration"], range=[0, 100])
st.pyplot()

st.write(
  "Looking at this histogram we can tell that the majority of reported UFO sightings last between 0 and 10 seconds. This means that many of our data providers only had a few seconds to make a judgement about what they saw, which could affect our data. This also means that many of these sightings could be explained by natural events as many of our data providers only had a few short seconds to make a conclusion from their observations. "
)

st.header("Hypothesis #4:")
st.subheader(
  "Does the observed shape of the UFO have any relation to how long the sightings lasts?"
)

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
  "Looking at this box plot we can see that the observed shape of the UFO is independent of the length of the sighting. This could potentially be explained due to  most of the lengths being very close to each other with the graph only having a range of 15 seconds. This means that many people still don't have enough time to make a precise judgement about what shape they think the UFO was, leading to similar results in the graph's time interval."
)

st.header("Hypothesis #5:")
st.subheader("Is there a specific shape of UFO that is more commonly reported in UFO sightings than others?")

top_10_states = df['Shape'].value_counts().head(5)

st.title("Fill Between Chart: Top 10 States")
st.area_chart(top_10_states)


top_10_states = df['Shape'].value_counts().head(20)
st.plotly_chart(
  px.pie(top_10_states,
         values=top_10_states,
         names=top_10_states.index,
         title="Shapes of UFO's"))

st.write("These graphs show the most common shapes of UFO's are light, circle, and triangle.")

st.header("Hypothesis #6:")
st.subheader("Does the country have anything to do with the shape of the UFO?")

USA = df[df["Country"] == "USA"].head(20)
df = df[df['Shape'] != 'Unknown']

top_10_states = USA['Shape'].value_counts().head(20)

st.plotly_chart(
  px.bar(top_10_states,
         x=top_10_states.index,
         y=top_10_states.values,
         title="Shapes of UFO's in the USA"))

UK = df[df["Country"] == "United Kingdom"].head(20)
df = df[df['Shape'] != 'Unknown']

top_10_states = UK['Shape'].value_counts().head(20)

st.plotly_chart(
  px.bar(top_10_states,
         x=top_10_states.index,
         y=top_10_states,
         title="Shapes of UFO's in the USA"))

CAN = df[df["Country"] == "Canada"].head(20)
df = df[df['Shape'] != 'Unknown']

top_10_states = CAN['Shape'].value_counts().head(20)
st.plotly_chart(
  px.bar(top_10_states,
         x=top_10_states.index,
         y=top_10_states,
         title="Shape's of UFO's in Canada"))

AUS = df[df["Country"] == "Australia"].head(20)

top_10_states = AUS['Shape'].value_counts().head(20)
st.plotly_chart(
  px.bar(top_10_states,
         x=top_10_states.index,
         y=top_10_states,
         title="Shape's of UFO's in Australia"))

st.write(
  "These graphs show that in different countries both light and circle are towards the top of the most common but the order of the other shapes is very different. Therefore to an extent where you live matters for the shapes of UFO's you will see."
)

st.header("Hypothesis #7:")
st.header("What can we tell about the time of UFO sightings?")

top_10_states = df["Time"].value_counts().head(200)

st.title("Times of UFO visits")
st.line_chart(top_10_states)

st.write("As you can see from the chart, most of the UFOs are seen at night.")

st.header("Hypothesis #8:")
st.header("Where do we have the most images of UFOs")


dff = df[df["Images"] == "Yes"].head(200)

top_5 = dff['Country'].value_counts().head(5)


st.plotly_chart(
  px.pie(top_5,
         values=top_5.values,
         names=top_5.index,
         title="Top 5 Countries with UFO Sightings"))

st.write("As you can see from the chart, most images are from USA.")

st.header("Conclusion :")

st.write (" So, In this data science project on UFO sightings, we analyzed the data to find that the United States had the highest number of reported sightings, most sightings lasted between 0 and 10 seconds, and common shapes reported were light, circle, and triangle. ")


