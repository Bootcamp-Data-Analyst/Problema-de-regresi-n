
# Problema de regresion Python & Machine Learning

En este proyecto, tenemos como objetivo escoger un dataset de nuestra preferencia en https://www.kaggle.com/, limpiar el dataset, y entrenarlo cun un modelo de machine learning, escogimos este dataset https://www.kaggle.com/datasets/taeefnajib/used-car-price-prediction-dataset

## 📊 Tabla de Datos de Vehículos

| Campo | Descripción |
|------|-------------|
| Brand & Model | Marca del vehículo junto con el modelo específico. |
| Model Year | Año de fabricación del vehículo. |
| Milage | Kilometraje registrado del vehículo. |
| Fuel Type | Tipo de combustible que utiliza el vehículo (gasolina, diésel, eléctrico o híbrido). |
| Engine | Tipo y especificaciones del motor, relacionadas con rendimiento y eficiencia. |
| Transmission | Tipo de transmisión del vehículo (automática, manual u otra). |
| Ext_Col | Color exterior del vehículo. |
| Int_Col | Color del interior del vehículo. |
| Accident | Indica si el vehículo tiene historial de accidentes o daños previos. |
| Clean Title | Especifica si el vehículo cuenta con un título limpio, relevante para su valor legal y de reventa. |
| Price | Precio de venta del vehículo. |

## 📊 Limpieza y Preparación de Datos

Durante el desarrollo del proyecto se realizaron las siguientes tareas de limpieza y preprocesamiento de datos:

### ✅ Features implementadas

- **Eliminación de columnas innecesarias**
  - Se eliminó la columna `clean_title` por no aportar valor al análisis.

- **Tratamiento de valores nulos**
  - En la columna `accident`, las celdas vacías fueron rellenadas con el valor `"None reported"` para mantener consistencia en los datos.

- **Corrección de tipos de datos**
  - Se realizó el cambio de tipado en las columnas:
    - `milage`
    - `price`
  - Se eliminaron caracteres no numéricos como `$` y `,`, reemplazándolos por `.` cuando fue necesario, permitiendo su correcta conversión a valores numéricos.

Estas transformaciones aseguran una mayor calidad de los datos y permiten un análisis más fiable y consistente.


## Demo

Por ahora no tenemos una demo en vivo del modelo machine learning, lo mismo usaremos Streamlit, Gradio, Etc...


## 👥 Colaboradores

[![GitHub Leonkeneddy86](https://img.shields.io/badge/GitHub-Leonkeneddy86-181717?style=for-the-badge&logo=github)](https://github.com/Leonkeneddy86)
[![GitHub Frodmar](https://img.shields.io/badge/GitHub-Frodmar-181717?style=for-the-badge&logo=github)](https://github.com/Frodmar)
[![GitHub RubenCG1997](https://img.shields.io/badge/GitHub-RubenCG1997-181717?style=for-the-badge&logo=github)](https://github.com/RubenCG1997)

