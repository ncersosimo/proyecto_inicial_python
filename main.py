# Proyecto Integrador Curso Python Inicial
# Dictado por Inove School
# Alumno: Nicolas Cersosimo
# GitHub: https://github.com/ncersosimo/proyecto_inicial_python.git

import random, interfaz

def leer_palabra_secreta(palabras):
    # utilizo la función choice del módulo
    # ramdom para seleccionar de forma aleatoria
    # una palabra dento de la lista palabras
    palabra_seleccionada = random.choice(palabras)
    return palabra_seleccionada


def pedir_letra(letras_usadas):
    # Inicializo las variables a utilizar.
    cadena_1 = "Ingrese"
    cadena_2 = ""

    while True:
        # Solicito al usuario el ingreso de una letra.
        letra_ingresada = str(input(f"{cadena_1} una {cadena_2}letra"
                                    + " del alfabeto(a-z):\n")).lower()
        # Verifico si la longitud de
        # lo ingresado por el usuario es uno 
        if len(letra_ingresada) == 1:
            # Verifico si el caracter ingresado es
            # una letra del alfabeto (a-z)
            if letra_ingresada.isalpha():
                # Verifico que si la letra no ha sido ingresada
                # la guardo en la lista
                if letra_ingresada not in (letras_usadas):
                    letras_usadas.append(letra_ingresada)
                    break                
                else:
                    # Si la letra ha sido ingresada con anterioridad
                    print(f"La letra '{letra_ingresada}'"
                          + " ya ha sido ingresada!")                    
                    cadena_1 = "ingrese"
                    cadena_2 = "nueva "
                    print("Por favor, ", end="")
            else:
                # Si el caracter no es una
                # letra del alfabeto (a-z)
                cadena_1 = "ingrese"
                cadena_2 = ""
                print(f"El caracter '{letra_ingresada}' no es una letra."
                      + " Por favor, ", end="")
        elif len(letra_ingresada) > 1:
            # Si se ha ingresado más de un caracter
            cadena_1 = "ingrese"
            cadena_2 = ""
            print("Debe ingresar un caracter a la vez. Por favor, ", end="")
        elif len(letra_ingresada) == 0:
            # Si no se ha ingresado ningún caracter
            cadena_1 = "ingrese"
            cadena_2 = ""
            print("Debe ingresar un caracter. Por favor, ", end="")
    return letra_ingresada


def verificar_letra(letra, palabra_secreta):
    # Verifico que la letra ingresada
    # es parte de la palabra secreta a adivinar
    if letra in (palabra_secreta):
        letra_valida = True
    else:
        letra_valida = False    
    return letra_valida


def validar_palabra(letras_usadas, palabra_secreta):
    # Inicializo la variable
    cantidad_letras = 0
    # Recorro las letras ingresadas por el usuario
    for caracter in range(len(letras_usadas)):
        # Recorro las letras de la palabra secreta
        # a adivinar
        for letra in range(len(palabra_secreta)):
            # Por cada letra de las letras ingresadas por el usuario
            # Verifico si se encuentra en la palabra secreta
            if letras_usadas[caracter] == palabra_secreta[letra]:
                # Si coinciden, la sumo a la variable cantidad_letras
                cantidad_letras += 1
    # Verifico que las letras ingresadas por el usuario
    # puedan formar la palabra secreta a adivinar
    if cantidad_letras == len(palabra_secreta):
        return True
    else:
        return False


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