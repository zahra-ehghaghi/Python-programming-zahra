import  streamlit as st
from send_email import send_email
st.header("Contact Me")
with st.form(key="email_form"):
    emial_address = st.text_input("Your Email Address")
    message = st.text_area("Enter message")
    message = f"""\n
    Subject: new email from {emial_address}\n
    
    From: {emial_address} 
    {message}    
"""
    button = st.form_submit_button("Submit")
if button:
    send_email(message)
    st.info("The email was sent out")
