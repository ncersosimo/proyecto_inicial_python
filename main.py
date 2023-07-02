import random, interfaz

def leer_palabra_secreta(palabras):
    # utilizo la función choice del módulo
    # ramdom para seleccionar de forma aleatoria
    # una palabra dento de la lista palabras
    palabra_seleccionada = random.choice(palabras)
    return palabra_seleccionada


def pedir_letra(letras_usadas):
    cadena = ""
    while True:
        letra_ingresada = str(input(f"Ingrese una {cadena}letra:\n")).lower()
        if letra_ingresada in (letras_usadas):
            print("La letra ingresada ya ha sido utilizada!!!")
            cadena = "nueva "
        else:
            letras_usadas.append(letra_ingresada)
            break
    return letra_ingresada


def verificar_letra(letra, palabra_secreta):
    if letra in (palabra_secreta):
        letra_valida = True
    else:
        letra_valida = False    
    return letra_valida


def validar_palabra(letras_usadas, palabra_secreta):
    palabra_valida = True
    return palabra_valida


if __name__ == "__main__":
    print("\n¡Aquí comienza el juego del ahorcado!\n")
    # Inicializo las variables y listas a utilizar.
    max_cantidad_intentos = 7
    intentos = 0
    letras_usadas = []
    es_ganador = False

    # Leer la palabra secreta de una lista.
    palabras = ["listas", "bucles", "variables"]
    palabra_secreta = leer_palabra_secreta(palabras)
    print(f"palabra_secreta: {palabra_secreta}")

    # Esto se realiza para que el jugador pueda ver al principio
    # la cantidad de letras de la palabra a adivinar.
    interfaz.dibujar(palabra_secreta, letras_usadas, intentos)
    
    while intentos < max_cantidad_intentos and not es_ganador:
        # Pedir una nueva letra
        letra = pedir_letra(letras_usadas)

        # Verificar si la letra es parte de la palabra secreta        
        if verificar_letra(letra, palabra_secreta) == False:
            # En caso de no estar la letra ingresada en la palabra
            # a adivinar incremento en 1 la variable intentos.
            intentos += 1
        
        # Dibujar la interfaz
        interfaz.dibujar(palabra_secreta, letras_usadas, intentos)

        # Validar si la palabra secreta se ha adivinado
        if validar_palabra(letras_usadas, palabra_secreta) == True:
            es_ganador = True
            break

    if es_ganador:
        print(f'\n¡Usted ha ganado la partida!, palabra secreta {palabra_secreta}!\n')
    else:
        print('\n¡Ahorcado!')
        print(f'\n¡Usted ha perdido la partida!, palabra secreta {palabra_secreta}!\n')