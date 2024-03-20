import streamlit as st
from sobre_mi import sobre_mi
from contacto import contacto
import os
from formacion import formacion
from experiencia import experiencia
from cv import cv

estilo_css = """
        <style>
            /* Cambiar el fondo principal */
            body {
                background-color: #f0f0f0; /* Cambia el color de fondo principal */
            }

            /* Cambiar el fondo lateral */
            .sidebar {
                background-color: #333; /* Cambia el color de fondo lateral */
                color: black; /* Cambia el color del texto a negro */
            }
        </style>
    """

    # Mostrar el estilo CSS
    st.markdown(estilo_css, unsafe_allow_html=True)


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


if __name__ == "__main__":
     main()

