import streamlit as st
import cv2
import pytesseract
from PIL import Image
import numpy as np

st.title("Document Scanner Application")

upload = st.file_uploader("please upload an Image", type=['jpg', 'png', 'jpeg'])

def extract_text(img):
    text = pytesseract.image_to_string(img)
    return text
if upload is not None:
    image = Image.open(upload)
    image_array = np.array(image)
    st.image(image_array, caption="uploaded Image")

    with st.spinner("Extracting text from ur Image..."):
        text = extract_text(image_array)
        st.subheader("Text Scanned")
        text_list = text.splitlines()
        st.write(" ".join(text_list))