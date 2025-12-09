# Desafio 125: Programa que aplique un filtro de dibujo animado a la camara

import cv2
import numpy as np

def cartoon_filter(img):
    img_color = cv2.bilateralFilter(img, d=9, sigmaColor=300, sigmaSpace=300)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    edges = cv2.adaptiveThreshold(
        img_gray, 
        255, 
        cv2.ADAPTIVE_THRESH_MEAN_C, 
        cv2.THRESH_BINARY, 
        blockSize=9,  # Un bloque pequeño
        C=2
    )

    edges = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    cartoon_img = cv2.bitwise_and(img_color, edges)
    
    return cartoon_img

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
        
    output_frame = cartoon_filter(frame)
    
    cv2.imshow('Filtro de Dibujo Animado', output_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# Explicacion: Se capturan los frames con la camara y a cada frame se le aplica un filtro animado. Se detectan bordes para simular un contorno animado y se reduce la paleta de colores para las areas de color plano.
