import streamlit as st
from PIL import Image

def contacto():
    st.title("¿Donde me puedes encontrar?")

    # Mostrar imagen del teléfono

    chincheta_emoti = "📍"
    direccion = "Santiago de Compostela"
    st.write(f"{chincheta_emoti} {direccion}")


    telefono_emoti = "📞"
    numero_telefono = "667 23 49 39"
    st.write(f"{telefono_emoti} {numero_telefono}")

    correo_emoti = "📩 "
    correo = "aidaamoedo@hotmail.com"
    st.write(f"{correo_emoti}{correo}")

    # Cargar el logo de LinkedIn
    image = Image.open("logos/linkedin.png")

    # Mostrar el logo y la frase lado a lado
    col1, col2 = st.columns([1, 30])
    with col1:
        st.image(image, width=20)
    with col2:
        st.write("www.linkedin.com/in/aida-amoedo")

    # Cargar el logo de github
    image2 = Image.open("logos/github.png")

    # Mostrar el logo y la frase lado a lado
    col1, col2 = st.columns([1, 30])
    with col1:
        st.image(image2, width=20)
    with col2:
        st.write("https://github.com/aidamoo")







if __name__ == "__main__":
    contacto()