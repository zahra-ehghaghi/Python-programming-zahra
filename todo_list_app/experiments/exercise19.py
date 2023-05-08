import streamlit as st
from PIL import Image

uploaded_image = st.file_uploader("Upload Image")
print(uploaded_image)
with st.expander("Start Camera"):
    camera_image = st.camera_input("Camera")

if camera_image:
    img = Image.open(camera_image)
    gray_img = img.convert("L")
    st.image(gray_img)
elif uploaded_image:
    img = Image.open(uploaded_image)
    gray_img = img.convert("L")
    st.image(gray_img)
