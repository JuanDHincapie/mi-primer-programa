"""
crea un programa que te cuente el numero de vocales y consonantes dentro de una frase introducida por el usuario
"""

frase_usuario = input("introduce una frase: ")

vocales = ["a", "e", "i", "o", "u"]

n_vocales = 0
n_consonantes = 0

for letra in frase_usuario:
    if letra in vocales:
        n_vocales += 1
    else:
        n_consonantes += 1

print("las vocales son {}".format(n_vocales))
print("las consonantes son {}".format(n_consonantes))

