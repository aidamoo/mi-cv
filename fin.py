import streamlit as st
from PIL import Image

def fin():
    st.write(" ")
    st.write(" ")
    st.write(" ")

    image = Image.open(
        "imagenes/fin.PNG")
    st.image(image=image, width=800)

if __name__ == "__main__":
    fin()