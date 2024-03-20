import streamlit as st
import textwrap

def experiencia():
    st.title("Experiencia")
    st.subheader("**Talent Consultant Professional - Manpower**")
    st.write("**Abril 2022 - Septiembre 2023**")
    st.write("Encargada de la gestión de los procesos de selección área Galicia de principio a fin:")
    st.write("- Elaboración de Briefing.")
    st.write("- Publicación de oferta y búsqueda directa de candidatos/as.")
    st.write("- Criba curricular.")
    st.write("- Entrevistas personales.")
    st.write("- Gestión base de datos.")
    st.write("- Elaboración de informes para posterior envío a cliente.")
    st.write("- Seguimiento procesos de selección con cliente.")
    st.write("- Cierre y facturación.")

    st.write(" ")

    st.subheader("**Talent Consultant - Manpower**")
    st.write("**Noviembre 2021 - Abril 2022**")
    st.write("Consultora de Trabajo Temporal. Trato directo con cliente, selección, altas/bajas, gestión de bajas médicas y absentismos, cierres...")

    st.write(" ")

    st.subheader("**HRBP SALES DT NORTE – Verisure Securitas Direct**")
    st.write("**Marzo 2020 - Octubre 2021**")
    texto1 = "- Planificación junto a la Dirección Territorial y Planificación Comercial de la estructura."
    texto_justificado = textwrap.fill(texto1, width=70)
    st.write(texto_justificado)
    texto2 = "- Búsqueda activa de candidatos/as a través de diferentes fuentes de reclutamiento, publicación de ofertas, criba curricular, entrevistas telefónicas, infomeeting, entrevistas personales, visualización de videoentrevistas..."
    texto_justificado2 = textwrap.fill(texto2, width=70)
    st.write(texto_justificado2)
    st.write("- Registro y seguimiento del FUNNEL de selección")
    st.write("Control y seguimiento de los registros relacionados con los empleados a través de Workday (bajas médicas, vacaciones, gestión de absentismos...)")
    st.write("- Gestionar y garantizar el Pool de talento (promociones internas).")

    st.subheader("**Prácticas RRHH – Complejo Hospitalario Pontevedra.**")
    st.write("**05/2019 – 06/2019**")

    st.write(" ")
    st.write(" ")
    st.write(" ")

    st.subheader("**Otras Experiencias:**")
    st.subheader("**Kameleon Vintage**")
    st.write("**10/2018 – Marzo 2019**")
    st.write("Tienda de ropa de segunda mano. Recepción de mercancía, gestión de envíos, trato directo con clientes.")


if __name__ == "__main__":
    experiencia()