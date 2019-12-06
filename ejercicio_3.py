"""Crea un programa que muestre por pantalla una lista de todas las vocales que aparecen en una string introducida por el usuario.

"""
frase_usuario = input("ingrese una frase corta: ")

vocales = ["a", "e", "i", "o", "u"]

for letra in frase_usuario:
    if letra == vocales[0]:
        print(vocales[0])
    elif letra == vocales[1]:
        print(vocales[1])
    elif letra == vocales[2]:
        print(vocales[2])
    elif letra == vocales[3]:
        print(vocales[3])
    elif letra == vocales[4]:
        print(vocales[4])
