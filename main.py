import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar los datos
df = pd.read_csv("./data/merged_df.csv")  # Reemplaza "tu_archivo.csv" con el nombre de tu archivo CSV

# Interfaz de usuario con Streamlit
st.title("Métricas")

# Seleccionar jugador
jugador = st.multiselect("Selecciona un jugador:", df['Jugador'].unique())

# Seleccionar columna
columnas_disponibles = ['Errores No Forzados', 'Winners', 'Puntos Ganados de Remate',
                        '% Primeros Saques', '% Segundos Saques',
                        '% Puntos Ganados con Primeros Saques', '% Puntos Ganados con Segundos Saques',
                        'Dobles Faltas', 'Km Recorridos', 'Puntos de Break', 'Puntos de Oro',
                        'Errores No Forzados de Fondo de Pista', 'Errores No Forzados en Red',
                        '% de Restos Fallados']
columna_seleccionada = st.selectbox("Selecciona una columna:", columnas_disponibles)
print("----columna_seleccionada-----")
print(columna_seleccionada)

# Filtrar datos del jugador seleccionado
if st.button('Mostrar'):
    print("---------")
    print(jugador)
    datos_jugador = df[df['Jugador'].isin(jugador)]
    print("----datos_jugador-----")
    print(datos_jugador)
    # Crear la visualización
    # Crear la visualización
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=datos_jugador, x='Partido', y=columna_seleccionada, hue="Jugador", ci=None)
    plt.xticks(range(1,21))
    plt.title(f"{columna_seleccionada} para {jugador}")
    plt.xlabel("Partido")
    plt.ylabel(columna_seleccionada)
    st.pyplot(plt)


