

import random

#Juego de ahorcados con colores
def elegir_color():

    lista = ['rojo', 'negro', 'amarillo','azul','blanco', 'verde', 'rosa', 'violeta', 'marron', 'celeste']
    return random.choice(lista)

def mostrador_de_resultado(color_secreto,letras_adivinadas):

    palabra = ''
    
    for letra in color_secreto:
        if letra in letras_adivinadas:
            palabra += letra
        else:
            palabra += '_'
    
    return palabra

def juego_ahorcados():
    color_secreto = elegir_color()
    intentos = 7
    juego_terminado = False
    letras_adivinadas = []

    print("Bienvenido al juego de los ahorcados para encontrar colores")
    print(f"Tienes {intentos} intentos")
    mostrador_de_resultado(color_secreto, letras_adivinadas)

    while not juego_terminado or intentos > 0:
        mostrador_de_resultado(color_secreto, letras_adivinadas)
        letra = input("Ingrese una letra por favor: ")
        
        if len(letra) != 1 or not letra.isalpha():
            print("por favor ingresa  una sola letra")
        elif letra in letras_adivinadas:
            print("ya has elegido esta letra escoge otra")
        else:
            letras_adivinadas.append(letra)

            if letra in color_secreto:
                print("felicidades has encontrado una letra del color secreto")
                letras_adivinadas.append(letra)
            else:
                print("mala suerte la letra no esta en el color secreto")
                intentos -= 1
                print(f"te quedan {intentos} intentos")
        
        actualizador = mostrador_de_resultado(color_secreto,letras_adivinadas)
        print(actualizador)
    
        if "_" not in actualizador:
            print("Felicidades has ganado, has encontrado el color correcto.")
            juego_terminado = True
            return
            


    if intentos  == 0:
        print("Has perdido, el color que  buscabas es '{color_secreto}'")

juego_ahorcados()




