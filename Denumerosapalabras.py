from num2words import num2words

def numero_a_palabras(numero):
    parte_entera = int(numero)
    parte_decimal = int(round((numero - parte_entera) * 100))
    palabras_enteras = num2words(parte_entera, lang='es')
    return f"{palabras_enteras} pesos {parte_decimal}/100 M.N."

print("Bienvenido al convertidor de números a palabras para cheques")
numero= None
while numero is None:
    try:
        numero = float(input("Dame un número: "))
        if numero < 0:
            print("No se aceptan cantidades negativas")
            numero = None
            continue
        print(numero_a_palabras(numero))
    except ValueError:
        print("Eso no es un número")
        continue