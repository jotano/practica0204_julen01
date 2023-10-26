palabra_inversa = input("Escribe una palabra:")
longitud = len(palabra_inversa)
orden_letra = longitud - 1
while orden_letra >= 0:
    letra = palabra_inversa[orden_letra]
    print(letra)
    orden_letra -= 1
input("Pulsa enter para salir")
