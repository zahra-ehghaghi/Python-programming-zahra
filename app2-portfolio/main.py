import streamlit as st
st.set_page_config(layout="wide")
col1, col2 = st.columns(2)
with col1:
    st.image("images/photo.png")

with col2:
    st.title("Zahra Ehghaghi")
    content = """
    Highly dedicated and responsible professional looking for a position as a software development.
    Resourceful and versatile IT professional with about 15 years of experience in software development and software architecture, with extensive practice in JAVA development. Familiar with well-practiced in all phases of Software Development Life Cycle (SDLC) with analysis, design, coding, testing and deployment using JAVA technologies.
    Having more than 6+ years hands on experience on OFM (10g , 11g and 12c). Familiar with oracle stack products and capable of offering and implementing architecture and solution for enterprise issues such as integration (data and process), SOA Governance, Security, service registry with oracle products.
    Capable of working individually or as a member of team to providing high quality service to every project. Professional, flexible, capable, and motivated individual who consistently performs in challenging environments. Eager to learn new materials and ready for new challenges.
    """
    st.info(content)
content="""
Below you can fine someof the apps i have built in Python. Feel free to contact me!
"""
st.write(content)

