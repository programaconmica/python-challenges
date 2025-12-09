# Desafio 124: Programa que detecte sonrisas en la camara

import cv2

smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
        
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    smiles = smile_cascade.detectMultiScale(gray, scaleFactor=1.7, minNeighbors=22)
    
    for (x, y, w, h) in smiles:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
    
    cv2.imshow('Detección de Sonrisas', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# Explicación: El programa utiliza OpenCV para capturar video desde la cámara web y detectar sonrisas en tiempo real usando un clasificador Haar Cascade preentrenado. Las sonrisas detectadas se resaltan con rectángulos rojos en el video.
