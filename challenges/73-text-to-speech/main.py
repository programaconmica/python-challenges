# Desafia 73: Funcion para convertir de texto a voz

# pip install gTTS playsound

from gtts import gTTS
from playsound import playsound
import os

def texto_a_voz(texto, lang="es"):
    tts = gTTS(texto, lang=lang)
    archivo = "voz.mp3"
    tts.save(archivo)
    playsound(archivo)
    os.remove(archivo)
    
texto_a_voz("Hola, este es un texto convertido a voz.")
