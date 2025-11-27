# Desafio 67: Detectar colores en tiempo real con la cámara

# pip install opencv-python

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    color = frame[frame.shape[0]//2, frame.shape[1]//2]  # Color en el centro
    b, g, r = int(color[0]), int(color[1]), int(color[2])
    frame[:] = [b, g, r]  # Cambia todo el frame al color detectado
    cv2.putText(frame, f"RGB: ({r},{g},{b})", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    cv2.imshow("Color Detector", frame)
    if cv2.waitKey(1) & 0xFF == 27:  # Presiona 'Esc' para salir
        break
cap.release()
cv2.destroyAllWindows()
