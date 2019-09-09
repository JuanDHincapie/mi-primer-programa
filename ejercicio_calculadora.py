operacion_elegida = input('¿Que operacion deseas hacer? ( sumar / restar / multiplicar / dividir): ')
while operacion_elegida != "FIN":
    if operacion_elegida == "sumar":
        print("Selecciona dos numeros: ")
        primer_numero = int(input("primer numero: "))
        segundo_numero = int(input("segundo numero: "))
        resultado_suma = primer_numero + segundo_numero
        print("si a {} se le suma {}, el resultado es de".format(primer_numero, segundo_numero))
        print(resultado_suma)
    elif operacion_elegida == "restar":
        print("Selecciona dos numeros: ")
        primer_numero = int(input("primer numero: "))
        segundo_numero = int(input("segundo numero: "))
        resultado_resta = primer_numero - segundo_numero
        print("si a {} se le restan {}, el resultado es de".format(primer_numero, segundo_numero))
        print(resultado_resta)
    elif operacion_elegida == "multiplicar":
        print("Selecciona dos numeros: ")
        primer_numero = int(input("primer numero: "))
        segundo_numero = int(input("segundo numero: "))
        resultado_multiplicacion = primer_numero * segundo_numero
        print("si a {} se le multiplica por {}, el resultado es de".format(primer_numero, segundo_numero))
        print(resultado_multiplicacion)
    elif operacion_elegida == "dividir":
        print("Selecciona dos numeros: ")
        primer_numero = int(input("primer numero: "))
        segundo_numero = int(input("segundo numero: "))
        resultado_division = primer_numero / segundo_numero
        print("si a {} se le divide en {}, el resultado es de".format(primer_numero, segundo_numero))
        print(resultado_division)
