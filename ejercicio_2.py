"""Crea un programa que sea capaz de contar espacios, puntos y comas en una string introducida por el usuario.
"""

frase_usuario = input("Escribe una frace con signos de puntuacion: ")

s_puntuacion = [".", ",", " "]

n_puntos = 0
n_comas = 0
n_espacios = 0

for letra in frase_usuario:
    if letra == s_puntuacion[0]:
        n_puntos += 1
    elif letra == s_puntuacion[1]:
        n_comas += 1
    elif letra == s_puntuacion[2]:
        n_espacios += 1

print("el numero de puntos en la frase es {}".format(n_puntos))

print("el numero de comas en la frase es {}".format(n_comas))

print("el numero de espacios en la frase es {}".format(n_espacios))

