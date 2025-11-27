# Desafío 77: Detectar caras en una imagen usando OpenCV

# pip install opencv-python

import cv2
import matplotlib.pyplot as plt

def detectar_caras(imagen_path):
    # Cargar el clasificador preentrenado para detección de caras
    cascada = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    # Leer la imagen
    imagen = cv2.imread(imagen_path)
    gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    
    # Detectar caras
    caras = cascada.detectMultiScale(gris, scaleFactor=1.1, minNeighbors=5)
    
    # Dibujar rectángulos alrededor de las caras detectadas
    for (x, y, w, h) in caras:
        cv2.rectangle(imagen, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    # Mostrar la imagen con las caras detectadas
    plt.imshow(cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show()
    
detectar_caras('foto.jpg')  # Asegúrate de tener una imagen llamada foto.jpg
