edad = int(input("Introduce la edad que tienes:"))
if edad <= 0:
    print("No se admiten a personas de 0 años")
else:
     for i in range(1, edad + 1):
       print (i)
input("Pulsa enter para salir")