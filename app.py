import streamlit as st
import plotly.express as px
import pandas as pd

car_data = pd.read_csv('vehicles_us.csv') # leer los datos

st.header('Información de vehículos')

hist_button = st.button('Construir histograma') # crear un botón
        
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
    # crear un histograma
    fig_h = px.histogram(car_data, x="odometer")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_h, use_container_width=True)

disp_button = st.button('Construir gráfico de dispersión') # crear un botón
        
if disp_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
            
    # crear un gráfico de dispersión
    fig_d = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_d, use_container_width=True)
