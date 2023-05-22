import  streamlit as st
import  requests

apikey = "DEMO_KEY"
url = f"https://api.nasa.gov/planetary/apod?api_key={apikey}"
response = requests.get(url)
content = response.json()
image = requests.get(content['hdurl'])
st.title(content['title'])
st.image(image.content)
st.write(content['explanation'])
