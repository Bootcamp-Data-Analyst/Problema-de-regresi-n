import streamlit as st
import pandas as pd
import numpy as np

st.title("Panel de Control")
st.subheader("Métricas del modelo")

df = pd.read_csv("data_frame_a_leer", skiprows=3)

df = df[['Country Name'] + [str(year) for year in range(1960, 2023)]]
df.set_index('Country Name', inplace=True)

p = st.multiselect("✅ Selecciona países", df.index)
st.line_chart(df.loc[p].T)