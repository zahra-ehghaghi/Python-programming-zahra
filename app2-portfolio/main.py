import streamlit as st
st.set_page_config(layout="wide")
col1, col2 = st.columns(2)
with col1:
    st.image("images/photo.png")

with col2:
    st.title("Zahra Ehghaghi")
    content = """
    My name is zahra ehghaghi and i am very enthusiasm to learn new topics and i say welcome to new challenges
    """
    st.info(content)