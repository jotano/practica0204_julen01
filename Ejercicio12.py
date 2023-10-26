frase = input("Escribe una frase:")
letra_en_frase = input("Escribe una letra:")
cantidad_letras = 0
for caracter in frase:
    if caracter == letra_en_frase:
        cantidad_letras += 1
print("La letra", letra_en_frase, "aparece", cantidad_letras, "veces dentro de la frase que has escrito")
input("Pulsa enter para salir")