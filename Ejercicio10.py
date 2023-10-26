Contraseña = "contraseña"
while True:
    ingreso_contraseña = input("Introduce la contraseña:")
    if ingreso_contraseña == Contraseña:
        print("La contraseña es correcta")
        break
    else:
        print("La contraseña no es correcta")
input("Pulsa enter para salir")