# Desafio 86: Hacer una prediccion simple con regresión lineal

# pip install scikit-learn matplotlib

from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

# Datos (horas de estudio -> nota en examen)
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([50, 55, 65, 70, 80])

# Crear y entrenar modelo
modelo = LinearRegression()
modelo.fit(X, y)

# Predecir nota si estudia 6 horas
prediccion = modelo.predict([[6]])

plt.plot(X, y, 'o')
plt.plot(X, modelo.predict(X), color='red')
plt.scatter(6, prediccion, color='green')  # Punto de predicción
plt.show()

print(f"Predicción para 6 horas de estudio: {prediccion[0]:.2f}")
