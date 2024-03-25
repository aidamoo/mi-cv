import streamlit as st
from PIL import Image

def cv():
    st.title("Mi CV")

    image = Image.open(
        "imagenes/CV AIDA.png")
    st.image(image=image, width=800)

if __name__ == "__main__":
    cv()