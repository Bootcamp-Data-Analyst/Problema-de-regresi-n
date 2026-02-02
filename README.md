
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

## 📌 Informe Ejecutivo

### 🎯 Objetivo del proyecto
El objetivo principal de este proyecto es **desarrollar un modelo predictivo capaz de estimar el precio de un vehículo** a partir de sus características principales, aplicando un flujo completo de análisis de datos y machine learning.

El proyecto se plantea como una **simulación realista de un caso de negocio**, en el que una empresa del sector automovilístico podría necesitar:
- Estimar precios de mercado
- Comparar vehículos con características similares
- Apoyar decisiones de compra, venta o tasación

Además, el proyecto busca demostrar competencias técnicas clave en **Data Analysis y Data Science**, desde la exploración inicial de los datos hasta el despliegue de una solución funcional.

---

### 📊 Descripción del dataset y preparación de los datos
El dataset utilizado contiene información sobre vehículos, incluyendo variables tanto **numéricas** como **categóricas**, entre ellas:
- Precio del vehículo  
- Año de fabricación  
- Kilometraje  
- Potencia y cilindrada del motor  
- Marca  
- Tipo de transmisión  
- Color exterior, entre otras  

Uno de los principales retos del proyecto fue la **calidad del dato**, ya que el dataset original presentaba:
- Valores faltantes
- Valores codificados como `-1`
- Inconsistencias en variables categóricas
- Distribuciones muy sesgadas en algunas variables numéricas  

Durante la fase de *data cleaning* se llevaron a cabo tareas como:
- Limpieza y estandarización de variables categóricas
- Tratamiento específico de valores inválidos (`-1`) para evitar sesgos
- Conversión de tipos de datos
- Preparación del dataset para su uso en análisis y modelado  

El resultado final es un **dataset limpio, coherente y listo para el análisis exploratorio y la modelización**.

---

### 🔍 Análisis Exploratorio de Datos (EDA)
El Análisis Exploratorio permitió comprender en profundidad el comportamiento del precio y su relación con otras variables del dataset.

Durante esta fase se analizaron:
- Distribuciones de variables numéricas clave como precio, kilometraje, potencia y cilindrada
- Relación entre el precio y el año del vehículo
- Impacto del kilometraje en la depreciación
- Diferencias de precio entre marcas y tipos de transmisión
- Presencia de outliers y su influencia en los resultados  

Este análisis permitió **extraer insights relevantes**, como:
- Tendencias claras de depreciación según año y kilometraje
- Diferencias significativas de precio entre marcas
- Variables con mayor capacidad explicativa sobre el precio  

Los resultados del EDA fueron fundamentales para **guiar la selección de variables** utilizadas posteriormente en el modelo de machine learning.

---

### 🤖 Modelado y Machine Learning
Una vez comprendidos los datos, se desarrolló un modelo de **regresión supervisada** para predecir el precio del vehículo.

El proceso de modelado incluyó:
- Selección de variables relevantes basadas en el EDA
- Codificación de variables categóricas
- División del dataset en conjuntos de entrenamiento y test
- Entrenamiento de modelos de regresión
- Evaluación del rendimiento mediante métricas de error (MAE y RMSE)

Tras comparar los resultados, se seleccionó el modelo con **mejor equilibrio entre precisión y capacidad de generalización**.  
El modelo final fue serializado en un archivo `model.pkl` para su reutilización y despliegue.

---

### 🖥 Despliegue y aplicación interactiva
Como parte final del proyecto, se desarrolló una **aplicación web con Streamlit** que permite llevar el modelo a un entorno práctico y accesible.

La aplicación incluye:
- Una estructura de navegación clara (inicio, predicciones y dashboard)
- Un formulario para introducir las características de un vehículo
- Predicción del precio en tiempo real utilizando el modelo entrenado
- Visualización de datos y resultados de forma interactiva  

---

### 🛠 Tecnologías y herramientas utilizadas
- **Python**
- **Pandas** y **NumPy**
- **Matplotlib** y **Seaborn**
- **Scikit-learn**
- **Jupyter Notebook**
- **Streamlit**
- **Pickle**

---

### 💡 Valor añadido del proyecto
Este proyecto demuestra:
- Capacidad para abordar un problema real desde un enfoque analítico
- Dominio del flujo completo de un proyecto de datos
- Buen criterio en la limpieza y preparación del dato
- Capacidad de extraer conclusiones útiles a partir del EDA
- Habilidad para convertir un modelo en una aplicación funcional  

---

### 🚀 Líneas de mejora y trabajo futuro
Como posibles mejoras del proyecto se plantean:
- Feature engineering avanzado para mejorar el rendimiento del modelo
- Comparación con modelos más complejos (Random Forest, Gradient Boosting, XGBoost)
- Inclusión de métricas explicativas del modelo en la app
- Despliegue en la nube para acceso público



## Demo

Por ahora no tenemos una demo en vivo del modelo machine learning, lo mismo usaremos Streamlit, Gradio, Etc...


## 👥 Colaboradores

[![GitHub Leonkeneddy86](https://img.shields.io/badge/GitHub-Leonkeneddy86-181717?style=for-the-badge&logo=github)](https://github.com/Leonkeneddy86)
[![GitHub Frodmar](https://img.shields.io/badge/GitHub-Frodmar-181717?style=for-the-badge&logo=github)](https://github.com/Frodmar)
[![GitHub RubenCG1997](https://img.shields.io/badge/GitHub-RubenCG1997-181717?style=for-the-badge&logo=github)](https://github.com/RubenCG1997)

