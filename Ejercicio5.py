nombre = input("Escribe tu nombre:")
género= input("Escribe tu sexo, H para hombre y M para mujer:")
if (género == "M" and nombre < "m") or (género == "H" and nombre >= "n"):
    grupo = "Gryffindor"
else:
    grupo = "Slytherin"
print("Eres de",grupo)
input("Pulsa enter para salir")