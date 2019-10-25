"""
Crea un programa quesea capaz de contar las letras mayusculas dentro de una frase introducida por el ususario
"""

frase_usuario = input("escribe una frase que contenga mayusculas dentro: ")

mayusculas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
              "V", "W", "X", "Y", "Z"]

n_mayusculas = 0
n_minusculas = 0
for letra in frase_usuario:
    if letra in mayusculas:
        n_mayusculas += 1
    else:
        n_minusculas += 1
print("el numero de mayusculas es de {}".format(n_mayusculas))
print("el numero de minusculas es de {}".format(n_minusculas))
