import streamlit as st
import  plotly.express as px
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place:")
days= st.slider("Forcast Days", min_value=1, max_value=5,
                 help="Select the number of forcasted days")
option=st.selectbox("Select Data to view",("Temperature","Sky"))
st.subheader(f"{option} for the next {days} days in {place}")
def get_date(days):
    dates=["2022-25-10","2022-25-11","2022-25-12"]
    tempretures=[10,11,15]
    tempretures=[i*days for i in tempretures ]
    return  dates,tempretures
x,y = get_date(days)
figure= px.line(x=x,y=y,labels={"x":"Date", "y":"Tempreture(C)"})
st.plotly_chart(figure)

