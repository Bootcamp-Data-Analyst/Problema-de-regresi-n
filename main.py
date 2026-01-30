import streamlit as st

st.set_page_config(
    page_title="Demo",
    page_icon="SVG\machine-learning-svgrepo-com.svg", # Icono
    layout="wide"
)

# Definir estructura de navegación
try:
    pg = st.navigation([
    st.Page("pages/Inicio.py", title="Inicio",default=True),
    st.Page("pages/Prediccion.py", title="Predicciones del modelo"),
    st.Page("pages/Dashboard.py", title="Nuestro Dashboard"),
])
    pg.run()
except Exception as e:
    st.error("Error al renderizar las vistas de Streamlit.")
    if st.button("Reintentar"):
        st.experimental_rerun()