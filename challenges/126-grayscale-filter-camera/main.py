# Desafio 126: Programa que aplique un filtro de escala de grises a la camara

import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    if not ret:
        break

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    cv2.imshow('Filtro de Escala de Grises', gray_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# Explicación: El programa captura video desde la cámara web y convierte cada frame a escala de grises usando cv2.cvtColor(). Luego muestra el video en una ventana. El bucle continúa hasta que se presiona la tecla 'q' para salir.
