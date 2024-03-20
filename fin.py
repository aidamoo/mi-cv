import streamlit as st
from PIL import Image

def fin():

    image12 = Image.open(
        "logos/finn.PNG")
    st.image(image=image12, width=800)

if __name__ == "__main__":
    fin()