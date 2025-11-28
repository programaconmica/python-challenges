# Desafio 82: Hacer un programa que detecte manos en la camara

# pip install mediapipe opencv-python

import cv2
import mediapipe as mp

# Abrimos la cámara (índice 0 para la cámara predeterminada)
cap = cv2.VideoCapture(0)

# Inicializamos el modelo de MediaPipe para detección de manos
with mp.solutions.hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
) as manos:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("No se pudo capturar la imagen")
            break

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        resultado = manos.process(frame_rgb)

        if resultado.multi_hand_landmarks:
            for mano in resultado.multi_hand_landmarks:
                mp.solutions.drawing_utils.draw_landmarks(
                    frame,
                    mano,
                    mp.solutions.hands.HAND_CONNECTIONS
                )

        cv2.imshow('Detección de Manos', frame)

        if cv2.waitKey(5) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()
