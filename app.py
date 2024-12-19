import streamlit as st
import pandas as pd
import plotly.express as px

# Leer el archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado de la aplicación
st.header('Análisis de Vehículos Usados en EE. UU.')

# Botón para construir el histograma
hist_button = st.button('Construir histograma')
if hist_button: 
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Botón para construir el gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')
if scatter_button: 
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    fig = px.scatter(car_data, x="model_year", y="price", title='Precio vs. Año del Modelo', labels={'model_year': 'Año del Modelo', 'price': 'Precio'})
    st.plotly_chart(fig, use_container_width=True)


