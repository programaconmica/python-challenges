# Desafio 69: Detectar bordes en tiempo real con la cámara usando Canny Edge Detection

# pip install opencv-python

import cv2

cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convertir a escala de grises
    bordes = cv2.Canny(gris, 100, 200)  # Aplicar Canny Edge Detection
    cv2.imshow("Bordes", bordes)  # Mostrar los bordes detectados
    if cv2.waitKey(1) & 0xFF == 27:  # Presiona 'Esc' para salir
        break
cap.release()
cv2.destroyAllWindows()
