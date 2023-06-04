import  streamlit as st
import  plotly.express as px
import pandas as pd

df = pd.read_csv("happy.csv")
st.title("In Search of happiness")
options=["GDP","Happiness","Generosity"]
x_axis=st.selectbox("Select the data for the X-axis",options=options)
y_axis=st.selectbox("Select the data for the Y-axis",options=options)
figure= px.scatter(df,x=str(x_axis).lower(),y=str(y_axis).lower())
st.plotly_chart(figure)
