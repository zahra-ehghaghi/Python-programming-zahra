import streamlit as st
import pandas
st.set_page_config(layout="wide")
st.header("The Best Company")
content = """
A captive portal is what we call a network that requires your action before it allows you to connect to the Internet. This action could be to log in using a username and password, or just to accept the network's terms and conditions.
The way most networks do this is by redirecting you to such a page. Firefox will make automatic connections to detect these redirects. When those happen, you will see a notification indicating that you may need to log into the network. Normally, after you do this, the tab will be closed automatically. Occasionally, it will be kept around to display a message from the network's owners. 
"""
st.write(content)
st.subheader("Our Team")
col1,empty_col1, col2,empty_col2,col3 = st.columns([1.5,0.5,1.5,0.5,1.5])
df = pandas.read_csv("data.csv",sep=",")
length = len(df)/3
with col1:
    for index, row in df[:int(len(df)/3)].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row['role'])
        st.image(f"./images/{row['image']}")

with col2:
    for index, row in df[int(len(df)/3):int(len(df)/3)*2].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row['role'])
        st.image(f"./images/{row['image']}")

with col3:
    for index, row in df[int(len(df)/3)*2:].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row['role'])
        st.image(f"./images/{row['image']}")
