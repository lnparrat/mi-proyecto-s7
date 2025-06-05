import streamlit as st
import pandas as pd
import plotly.express as px

st.header('Análisis exploratorio')

car_data = pd.read_csv('vehicles_us.csv')
hist_button = st.button('Construir histograma')
disper_button = st.button('Construir gráfico de dispersión')

if hist_button:  # al hacer clic en el boton
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de anuncions de venta de coches')

    # crear un histograma
    hist = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Pllotly interactivo
    st.plotly_chart(hist, use_container_width=True)

if disper_button:
    st.write(
        'Creación de un gráfico de dispersión para el conjunto de anunciones de venta de coches')

    disper = px.scatter(car_data, x="odometer", y='price')

    st.plotly_chart(disper,  use_container_width=True)

# crear una casilla de verificacion
build_histogram = st.checkbox('Construir un histograma')

if build_histogram:
    st.write('Construir un histograma para la columna odómetro')
    # crear un histograma
    hist = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Pllotly interactivo
    st.plotly_chart(hist, use_container_width=True)
