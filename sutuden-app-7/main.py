import glob
import streamlit as st
import plotly.express as px
from nltk.sentiment import SentimentIntensityAnalyzer
filepathes = sorted(glob.glob("diary/*.txt"))

positive=[]
negative=[]
analyzer= SentimentIntensityAnalyzer()
for filepath in filepathes:
    with open(filepath) as file:
      content = file.read()
    scores=  analyzer.polarity_scores(content)
    positive.append(scores["pos"])
    negative.append(scores["neg"])
dates=[filepath.strip(".txt") .strip("diary/")for filepath in filepathes]

st.title("Diary Tone")
st.subheader("Positive")
ps_figure=px.line(x=dates,y=positive,labels={"x":"Date","y":"Positive"})
st.plotly_chart(ps_figure)

st.subheader("Negative")
ng_figure=px.line(x=dates,y=negative,labels={"x":"Date","y":"Negative"})
st.plotly_chart(ng_figure)


