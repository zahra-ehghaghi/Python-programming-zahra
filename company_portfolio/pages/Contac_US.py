import streamlit as st
import  pandas
from  send_email import  send_email


topics= pandas.read_csv("topics.csv")["topic"]
print(topics)
st.header("Contatc Me")
with st.form(key="send_email_form"):
    email_address= st.text_input("Your Email Address")
    topic = st.selectbox(label= "what topic do you want to discuss",
                            key="topic",options=topics)
    text = st.text_area("Text")
    button = st.form_submit_button("Submite")
if button:
    send_email(f"""\    
    Subject: New email to {email_address}
    
    From: {email_address}
    Topic: {topic} \n
    {text}
""")
    st.info("Email was sent successfully")



