primer_numero = float(input("Introduce el primer número a dividir: "))
segundo_numero = float(input("Introduce el segundo número a dividir: "))
if primer_numero == 0 or segundo_numero == 0:
    print("¡¡Error!!")
else:
    division = primer_numero / segundo_numero
    print("El resultado es: " + str(division))
input("Pulsa enter para salir")