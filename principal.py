import streamlit as st
from sobre_mi import sobre_mi
from contacto import contacto
import os
from formacion import formacion
from experiencia import experiencia
from cv import cv


def main():
    page = st.sidebar.radio("Menú", ("Introducción", "¿Quien soy?", "Formación", "Experiencia", "CV", "Contacto"))

    if page == "Introducción":
        st.title("Hola a todos/as")
        st.subheader("Bienvenidos/as a mi perfil")
        video_file = open("video/Welcome.mp4", "rb")
        video_bytes = video_file.read()
        st.video(video_bytes)

        pass

    elif page == "¿Quien soy?":
        sobre_mi()
        pass

    elif page =="Formación":
        formacion()
        pass

    elif page == "Experiencia":
        experiencia()
        pass

    elif page == "CV":
        cv()
        pass

    elif page == "Contacto":
        contacto()
        pass

    # Estilo CSS para cambiar el color de fondo de la barra lateral
    estilo_css = """
        <style>
            /* Cambiar el color de fondo de la barra lateral */
            .sidebar {
                background-color: #333; /* Cambia el color de fondo a un gris oscuro */
            }
            /* Cambiar el color del texto en la barra lateral */
            .sidebar .sidebar-content {
                color: white; /* Cambia el color del texto a blanco */
            }
        </style>
    """

    # Mostrar el estilo CSS
    st.markdown(estilo_css, unsafe_allow_html=True)


if __name__ == "__main__":
     main()

