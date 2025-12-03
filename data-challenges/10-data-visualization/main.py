# Desafio 10: Visualizar datos con Pandas y Matplotlib.

import pandas as pd
import matplotlib.pyplot as plt

datos = {
    'mes': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio'],
    'ventas': [150, 180, 220, 200, 250, 280],
    'clientes': [20, 25, 30, 28, 35, 40]
}

df = pd.DataFrame(datos)
print(df)

# Visualizar ventas por mes
plt.figure(figsize=(10, 5))
plt.plot(df['mes'], df['ventas'], marker='o', label='Ventas')
plt.plot(df['mes'], df['clientes'], marker='s', label='Clientes')
plt.title('Ventas y Clientes por Mes')
plt.xlabel('Mes')
plt.ylabel('Cantidad')
plt.legend()
plt.grid()
plt.show()

# Explicación: Este desafío te enseña cómo visualizar datos utilizando Pandas junto con Matplotlib. Aprenderás a crear gráficos de líneas para representar tendencias en los datos, lo cual es una habilidad esencial para el análisis y la presentación de datos.
