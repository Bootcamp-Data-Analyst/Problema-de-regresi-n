import streamlit as st

st.set_page_config(
    page_title="Demo",
    page_icon="SVG\machine-learning-svgrepo-com.svg", # Icono
    layout="wide"
)

# Definir estructura de navegación
pg = st.navigation([
    st.Page("pages/Inicio.py", title="Inicio",default=True),
    st.Page("pages/Dashboard.py", title="Dashboard"),
])
pg.run()