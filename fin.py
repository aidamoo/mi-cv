import streamlit as st
from PIL import Image

def fin():
    st.title("Gracias!")

    image6 = Image.open(
        "imagenes/finnn.jpg")
    st.image(image=image6, width=500)

if __name__ == "__main__":
    fin()