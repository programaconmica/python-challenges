# Desafia 72: Funcion que convierta texto a codigo morse

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': '/'
}

def texto_a_morse(texto):
    texto = texto.upper()
    morse = ' '.join(MORSE_CODE_DICT.get(char, '') for char in texto)
    return morse

# Ejemplo de uso
texto = "Hola Mundo"
morse = texto_a_morse(texto)
print(f"Texto: {texto}")
print(f"Morse: {morse}")

# Explicación: La función convierte cada letra del texto a su equivalente en código Morse usando un diccionario de mapeo.
