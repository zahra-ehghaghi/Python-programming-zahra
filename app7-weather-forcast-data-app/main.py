import streamlit as st
import  plotly.express as px
from backend import  get_date
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place:")
days= st.slider("Forcast Days", min_value=1, max_value=5,
                 help="Select the number of forcasted days")
option=st.selectbox("Select Data to view",("Temperature","Sky"))
st.subheader(f"{option} for the next {days} days in {place}")
if place:
    try:
        filter_date= get_date(city=place,forcatdays=days)
        if option == "Temperature":
            Temperatures = [dict["main"]["temp"]/10 for dict in filter_date]
            dates= [dict["dt_txt"] for dict in filter_date]
            figure = px.line(x=dates , y=Temperatures, labels={"x": "Date", "y": "Temperatures(C)"})
            st.plotly_chart(figure)
        if option == "Sky":
            filter_date = [dict["weather"][0]["main"] for dict in filter_date]
            images={"Clear":"images/clear.png","Clouds":"images/cloud.png","Rain":"images/rain.png","Snow":"images/snow.png"}
            filter_date_images=[images[image] for image in filter_date]
            st.image(filter_date_images,width=115)
    except KeyError:
        st.info("Error: That place does not exist")



