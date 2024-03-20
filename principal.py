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

    # Obtener la ruta del directorio del script actual
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Construir la ruta completa a la imagen de fondo
    imagen_ruta = os.path.join(script_dir, "imagenes", "fondo.png")

    # Estilo CSS para establecer el fondo y cambiar el color de la barra lateral
    estilo_css = f"""
        <style>
            body {{
                background-image: url("{imagen_ruta}");
                background-size: cover;
            }}
            /* Cambiar el color de fondo de la barra lateral */
            .sidebar .sidebar-content {{
                background-color: #ADD8E6; /* Azul claro */
            }}
        </style>
    """

    # Mostrar el estilo CSS
    st.markdown(estilo_css, unsafe_allow_html=True)


if __name__ == "__main__":
     main()

