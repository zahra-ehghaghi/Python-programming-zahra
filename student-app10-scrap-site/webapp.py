import  streamlit as st
import  plotly.express as px
import  pandas

df = pandas.read_csv("data.txt")
figure = px.line(x=df["date"], y=df["tempretur"])
st.plotly_chart(figure)
