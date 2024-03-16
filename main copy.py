import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar tus datos
data = pd.read_csv("tu_archivo.csv")

# Crear el gráfico utilizando seaborn
sns.barplot(x="Columna_X", y="Columna_Y", data=data)

# Ajustar el formato de los ticks del eje x
plt.xticks(rotation=45)  # Rotar las etiquetas para mejor legibilidad
plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: int(x)))  # Formatear los ticks como enteros

# Mostrar el gráfico en Streamlit
st.pyplot()
