import streamlit as st
from sobre_mi import sobre_mi
from contacto import contacto
import os
from formacion import formacion
from experiencia import experiencia
from cv import cv
from fin import fin


estilo_css = """
        <style>
            /* Cambiar el fondo principal */
            body {
                background-color: #f0f0f0; /* Cambia el color de fondo principal */
            }

            /* Cambiar el fondo lateral */
            .sidebar {
                background-color: #333; /* Cambia el color de fondo lateral */
                color: black; /* Cambia el color del texto a black */
            }
        </style>
    """

# Mostrar el estilo CSS
st.markdown(estilo_css, unsafe_allow_html=True)


def main():
    st.markdown("""
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-2Q77LCWEC6"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());

      gtag('config', 'G-2Q77LCWEC6');
    </script>
    """, unsafe_allow_html=True)

    page = st.sidebar.radio("Menú", ("Introducción", "¿Quien soy?", "Formación", "Experiencia", "CV", "Contacto", "Fin"))

    if page == "Introducción":
        st.title("Hola a todos/as")
        st.subheader("Bienvenidos/as a mi perfil")
        video_file = open("video/Welcome (1).mp4", "rb")
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

    elif page == "Fin":
        fin()
        pass


if __name__ == "__main__":
     main()

