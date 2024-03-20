import streamlit as st
from PIL import Image

def fin():
    st.title("Gracias!")
    image6 = Image.open(
        "imagenes/finnn.png")
    st.image(image=image6, width=450)

if __name__ == "__main__":
    fin()