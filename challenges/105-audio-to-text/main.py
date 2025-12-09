# Desafio 105: Convertir de audio a texto

# pip install SpeechRecognition

import speech_recognition as sr

def audio_a_texto(ruta_audio):
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(ruta_audio) as source:
            audio = recognizer.record(source)
        texto = recognizer.recognize_google(audio, language='es-ES')
        return texto
    except sr.UnknownValueError:
        return "No se pudo entender el audio."
    except sr.RequestError as e:
        return f"Error al solicitar resultados; {e}"
    
# Ejemplo de uso
ruta = "audio.wav"  # Asegúrate de tener un archivo de audio llamado audio.wav
resultado = audio_a_texto(ruta)
print("Texto reconocido:", resultado)

# Explicación: Usamos la librería SpeechRecognition para convertir un archivo de audio en texto. El método recognize_google utiliza el servicio de reconocimiento de voz de Google para transcribir el audio.
