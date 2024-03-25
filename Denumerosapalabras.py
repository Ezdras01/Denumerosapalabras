import inflect
from num2words import num2words

def numero_a_palabras(numero):
    palabras = num2words(numero, lang='es')
    return palabras

print(numero_a_palabras(123))