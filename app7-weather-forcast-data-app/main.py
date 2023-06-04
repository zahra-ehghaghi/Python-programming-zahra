import streamlit as st
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place:")
dates= st.slider("Forcast Days", min_value=1, max_value=5,
                 help="Select the number of forcasted days")
option=st.selectbox("Select Data to view",("Tempereture","Sky"))
st.subheader(f"{option} for the next {dates} days in {place}")

