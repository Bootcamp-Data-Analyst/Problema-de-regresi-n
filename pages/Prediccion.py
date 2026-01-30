import streamlit as st
import joblib
import pandas as pd
import numpy as np

st.title('Predicción de Precios de Vehículos')

# --- ENCODER TIPO LabelEncoder (custom, compatible con LabelEncoder) ---
class LabelEncoder:
    def __init__(self):
        self.classes_ = []
        self.class_to_int = {}

    def fit(self, values):
        uniques = pd.Series(values).dropna().unique().tolist()
        self.classes_ = list(uniques)
        self.class_to_int = {v: i for i, v in enumerate(self.classes_)}
        return self

    def transform(self, values):
        return [self.class_to_int.get(v, -1) for v in values]

    def transform_scalar(self, v):
        return self.class_to_int.get(v, -1)

# --- POSTPROCESADOR ---
class PostProcesador:
    def round_post(self, y):
        return np.round(y).astype(int)

# --- CARGA DEL MODELO ---
try:
    pipeline = joblib.load('model.pkl')
    st.success("Modelo cargado correctamente")
except Exception as e:
    st.error(f"Error al cargar el modelo: {e}")
    st.stop()

post = PostProcesador()

# --- CARGA DE CATEGORÍAS (para poblar selectboxes y encoders) ---
try:
    df = pd.read_csv('data/clean_data.csv')
except Exception as e:
    st.error(f"No se pudo leer 'data/clean_data.csv': {e}")
    st.stop()

brand_enc = LabelEncoder().fit(sorted(df['brand'].dropna().unique()))
fuel_enc = LabelEncoder().fit(sorted(df['fuel_type'].dropna().unique()))
ext_enc = LabelEncoder().fit(sorted(df['ext_col'].dropna().unique()))
int_enc = LabelEncoder().fit(sorted(df['int_col'].dropna().unique()))

# --- FORMULARIO DE PREDICCIÓN ---
with st.form("prediction_form"):
    st.header("Ingrese los datos del vehículo")

    model_year = st.number_input("Año del modelo", min_value=1990, max_value=2025, step=1)
    milage = st.number_input("Kilometraje", min_value=0, step=1000)
    cylinders = st.number_input("Cilindros", min_value=0, max_value=16, step=1)
    horsepower = st.number_input("Caballos de fuerza", min_value=0, step=10)
    engine_liters = st.number_input("Motor (litros)", min_value=0.0, max_value=20.0, step=0.1)

    marca = st.selectbox("Marca", brand_enc.classes_)
    fuel_type = st.selectbox("Combustible", fuel_enc.classes_)
    Color_del_exterior = st.selectbox("Color exterior", ext_enc.classes_)
    Color_del_interior = st.selectbox("Color interior", int_enc.classes_)

    submit_button = st.form_submit_button("Predecir Precio")

if submit_button:
    try:
        input_dict = {
            "model_year": [model_year],
            "milage": [milage],
            "engine_liters": [engine_liters],
            "cylinders": [cylinders],
            "horsepower": [horsepower],
            "fuel_type_label": [fuel_enc.transform_scalar(fuel_type)],
            "brand_label": [brand_enc.transform_scalar(marca)],
            "ext_col_label": [ext_enc.transform_scalar(Color_del_exterior)],
            "int_col_label": [int_enc.transform_scalar(Color_del_interior)],
            "model_label": [-1],  # por defecto, si no especificas modelo
        }

        # Asegurar orden de columnas que usó el entrenamiento
        columns_order = [
            "model_year", "milage", "engine_liters", "cylinders", "horsepower",
            "fuel_type_label", "brand_label", "ext_col_label", "int_col_label", "model_label"
        ]
        input_data = pd.DataFrame(input_dict)[columns_order]

        prediccion = pipeline.predict(input_data)
        prediccion_final = post.round_post(prediccion)[0]

        st.success(f"Precio predicho: ${prediccion_final:,.2f}")

        with st.expander("Detalles de la predicción"):
            st.write(f"**Marca:** {marca}")
            st.write(f"**Color exterior:** {Color_del_exterior}")
            st.write(f"**Color interior:** {Color_del_interior}")
            st.write(f"**Combustible:** {fuel_type}")
            st.write(f"**Año del modelo:** {model_year}")
            st.write(f"**Kilometraje:** {milage}")
            st.write(f"**Motor (litros):** {engine_liters}")
            st.write(f"**Cilindros:** {cylinders}")
            st.write(f"**Caballos de fuerza:** {horsepower}")
            st.write(f"**Precio sin redondear:** ${prediccion[0]:,.2f}")

    except Exception as e:
        st.error(f"Error al hacer la predicción: {e}")

# --- INFORMACIÓN ADICIONAL ---
st.markdown("---")
st.markdown("""
**Notas:**
- Las categorías para los selectboxes se obtienen de `data/clean_data.csv`.
- Las categorías desconocidas se codifican como `-1` antes de pasar al modelo.
- El postprocesador redondea la predicción al entero más cercano.
""")