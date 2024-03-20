import streamlit as st
from PIL import Image

def fin():

    image = Image.open(
        "imagenes/finn.PNG")
    st.image(image=image, width=800)

if __name__ == "__main__":
    fin()