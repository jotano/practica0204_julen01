numero = int(input("Introduce un número entero:"))
for i in range(numero, numero + 1):
    if i / 2 == i // 2:
        print("Éste número es par.")
    else:
        print("Éste es un número impar.")
input("Pulsa enter para salir")