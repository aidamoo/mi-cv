import streamlit as st
from PIL import Image
import textwrap


def sobre_mi():
    st.title("¿Quien soy?")

    image2 = Image.open(
     "imagenes/linkedin_aida.png")
    st.image(image=image2, width=900)

    st.subheader("¡Me presento!")
    texto1 = "Mi nombre es Aida y actualmente me encuentro en búsuqeda activa de empleo. ¡Quédate para conocerme!"
    texto_justificado = textwrap.fill(texto1, width=70)
    st.write(texto_justificado)

    image3 = Image.open(
        "imagenes/foto_linkedin3.2.jpg")
    st.image(image=image3, width=200)

    st.subheader("Ámbito académico")
    st.write("**\U0001F4D6¿Estás buscando un Graduado/a en ADE?\U0001F4D6**")
    respuesta = st.radio("Selecciona una opción:", ("Sí, por supuesto, me vendría genial!\U0001F600", "No \U0001F622..."))
    if respuesta == "Sí, por supuesto, me vendría genial!\U0001F600":
        st.write("Excelente, podría ser tu candidata!")
    else:
        st.write("Vaya, sigue leyendo, seguro que podremos dar match de todas formas 😉")

    texto2 = "En el ámbito académico, soy Graduada en Administración y Dirección de Empresas con un Máster en Recursos Humanos, además acabo de finalizar un Bootcamp en Data Science."
    texto_justificado2 = textwrap.fill(texto2, width=70)
    st.write(texto_justificado2)

    st.subheader("Ámbito laboral")
    st.write("**¿Estás buscando una persona con experiencia en selección de personal?👨‍🚀**")
    respuesta = st.radio("Selecciona una opción:", ("Sí, por supuesto, ¡Es justo lo que buscaba!", "No 😢..."))
    if respuesta == "Sí, por supuesto, ¡Es justo lo que buscaba!":
        st.write("Genial, ¡Sigamos hablando!")
    else:
        st.write("Todavía podemos hacer match 😉")


    texto3 = "En cuanto a mi trayectoria profesional se ha centrado en el área de RRHH, donde he adquirido una amplia experiencia y conocimientos en dos grandes multinacionales como Securitas Direct y MANPOWER, especialmente en selección de personal."
    texto_justificado3 = textwrap.fill(texto3, width=70)
    st.write(texto_justificado3)

    st.subheader("Tecnología")
    st.write("**¿Te gustaría trabajar con una apasionada de la tecnología?**")
    respuesta = st.radio("Selecciona una opción:", ("Sí, ¡¡POR SUPUESTO!!❤️", "No 😢..."))
    if respuesta == "Sí, ¡¡POR SUPUESTO!!❤️":
        st.write("Genial, ¡Sigamos!")
    else:
        st.write("Oh vaya...")

    texto4 = "Despues de centrarme estos últimos 3 años y medio en RRHH, decido hacer un parón laboral en Septiembre de 2023 para introducirme en el análisis de datos, realizando el Bootcamp."
    texto_justificado4 = textwrap.fill(texto4, width=70)
    st.write(texto_justificado4)
    texto5 = "Mi objetivo es poder unir mi pasión por las personas y la tecnología."
    texto_justificado5 = textwrap.fill(texto5, width=70)
    st.write(texto_justificado5)

    st.subheader("Y ahora una pregunta sobre tu empresa...")
    st.write("**¿Consideras que en tu empresa se pone al candidato/a en el centro?**")
    respuesta = st.radio("Selecciona una opción:", ("Sí, ¡POR SUPUESTO!❤️", "No 😢..."))
    if respuesta == "Sí, ¡POR SUPUESTO!❤️":
        st.write("MATCH 😍😍")
    else:
        st.write("No match 💔 😢")



    st.write("¡Gracias por considerar mi perfil!")



if __name__ == "__main__":
    sobre_mi()