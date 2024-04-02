import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def mostrar_formacion_reglada():
    st.subheader("Formación Reglada")

    st.write(" **- Administración y Dirección de Empresas**. Universidad de Santiago de Compostela.")
    st.write(" **- Máster en Organización del Trabajo y Gestión de RRHH.** Centro de Formación de la Cámara de Comercio de Madrid")
    st.write(" **- Data Science & Inteligencia Artificial.** HACK A BOSS")
    image5 = Image.open(
        "imagenes/hack a boss 2.PNG")
    st.image(image=image5, width=450)

    image6 = Image.open(
        "imagenes/Diapositiva2.PNG")
    st.image(image=image6, width=450)

    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")

def mostrar_certificados():
    st.subheader("**Certificados.**")

    st.write(" **- Conviértete en Reclutador IT - Especialización en Reclutamiento y Contratación de perfiles Tecnológicos.** RecruHack")
    image12 = Image.open(
        "imagenes/recruhack.png")
    st.image(image=image12, width=450)

    st.write(" **- Automatiza tus procesos de selección con Airtable**. Nocodehackers")
    image4 = Image.open(
        "imagenes/Diapositiva1.PNG")
    st.image(image=image4, width=450)

    st.write(" **- PRO-ACTIVATE: CÓMO IR POR DELANTE DE TUS CLIENTES Y CANDIDATOS. Manpower Academy**.")
    image7 = Image.open(
        "imagenes/proactivate.JPG")
    st.image(image=image7, width=450)

    st.write("**- Evaluación del volviéndose experto en LinkedIn Recruiter**. LinkedIn Talent Solutions")
    image8 = Image.open(
        "imagenes/linkedin1.PNG")
    st.image(image=image8, width=450)

    st.write("**- Excel with LinkedIn Recruiter Assessment**. LinkedIn Talent Solutions")
    image9 = Image.open(
        "imagenes/excel_linkedin.PNG")
    st.image(image=image9, width=450)

    st.write("**- Negociación en el proceso de selección**. Manpower Academy.")
    image10 = Image.open(
        "imagenes/negociacion.PNG")
    st.image(image=image10, width=450)

    st.write("**- Entrenamiento en Assesment Center y Entrevista por Competencia.** Manower Academy")
    image11 = Image.open(
        "imagenes/entrenamiento.JPG")
    st.image(image=image11, width=450)

    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")


def mostrar_habilidades():
    st.subheader("**Habilidades.**")

    # Cargar el logo de LinkedIn
    image = Image.open("logos/linkedin.png")

    # Mostrar el logo y la frase lado a lado
    col1, col2 = st.columns([1, 10])
    with col1:
        st.image(image, width=30)
    with col2:
        st.write("**- LinkedIn Recruiter**")

    # Cargar el logo de Infojobs
    image2 = Image.open("logos/infojobs.png")

     # Mostrar el logo y la frase lado a lado
    col1, col2 = st.columns([1, 10])
    with col1:
        st.image(image2, width=60)
    with col2:
        st.write("**- Infojobs**")

    # Cargar el logo de office
    image3 = Image.open("logos/office.png")

    # Mostrar el logo y la frase lado a lado
    col1, col2 = st.columns([1, 10])
    with col1:
        st.image(image3, width=60)
    with col2:
        st.write("**- Paquete office**")

    # Cargar el logo de workday
    image4 = Image.open("logos/workday.png")

    # Mostrar el logo y la frase lado a lado
    col1, col2 = st.columns([1, 10])
    with col1:
         st.image(image4, width=60)
    with col2:
        st.write("**- Workday**")

    # Cargar el logo de jupyter
    image5 = Image.open("logos/jupyter.png")

    # Mostrar el logo y la frase lado a lado
    col1, col2 = st.columns([1, 10])
    with col1:
        st.image(image5, width=60)
    with col2:
        st.write("**- Jupyter Notebook**")

    # Cargar el logo de python
    image6 = Image.open("logos/python.png")

    # Mostrar el logo y la frase lado a lado
    col1, col2 = st.columns([1, 10])
    with col1:
        st.image(image6, width=40)
    with col2:
        st.write("**- Python**")

    # Cargar el logo de mysql
    image7 = Image.open("logos/sql.png")

    # Mostrar el logo y la frase lado a lado
    col1, col2 = st.columns([1, 10])
    with col1:
        st.image(image7, width=60)
    with col2:
        st.write("**- MySQL**")

    # Cargar el logo de PySpark
    image8 = Image.open("logos/pyspark.png")

    # Mostrar el logo y la frase lado a lado
    col1, col2 = st.columns([1, 10])
    with col1:
        st.image(image8, width=60)
    with col2:
        st.write("**- PySpark**")

    # Cargar el logo de PySpark
    image9 = Image.open("logos/pycharm.png")

    # Mostrar el logo y la frase lado a lado
    col1, col2 = st.columns([1, 10])
    with col1:
        st.image(image9, width=40)
    with col2:
        st.write("**- Pycharm**")

    # Cargar el logo de streamlit
    image10 = Image.open("logos/streamlit.png")

    # Mostrar el logo y la frase lado a lado
    col1, col2 = st.columns([1, 10])
    with col1:
        st.image(image10, width=40)
    with col2:
        st.write("**- Streamlit**")

    # Cargar el logo de airtable
    image11 = Image.open("logos/airtable.png")

    # Mostrar el logo y la frase lado a lado
    col1, col2 = st.columns([1, 10])
    with col1:
        st.image(image11, width=40)
    with col2:
        st.write("**- Airtable**")

    # Cargar el logo de github
    image12 = Image.open("logos/github.png")

    # Mostrar el logo y la frase lado a lado
    col1, col2 = st.columns([1, 10])
    with col1:
        st.image(image12, width=40)
    with col2:
        st.write("**- GitHub**")

    st.write("**- Data Science**: Pandas, Numpy, request,BeautifulSoup, Selenium, Helium, Matplotlib, seaborn, plotly, folium, APIs...")
    st.write("**- Machine Learning**: Regresión lineal, múltiple y logística, KNN, decision trees, random forest, NLP, algoritmos genéticos, redes neuronales, recomendador (contenido y colaborativo.)")


def formacion():
    st.title("Formación, certificados y habilidades")

    # Mostrar las pestañas estáticas arriba
    page = st.sidebar.radio("Formación", ("Formación Reglada", "Certificados", "Habilidades"))

    # Mostrar el contenido de la pestaña seleccionada ocupando toda la página
    if page == "Formación Reglada":
        mostrar_formacion_reglada()
    elif page == "Certificados":
        mostrar_certificados()
    elif page == "Habilidades":
        mostrar_habilidades()


if __name__ == "__main__":
    formacion()