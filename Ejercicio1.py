variable = "contraseña"
contraseña = input("¿Cuál es su contraseña?")
variable = variable.lower()
contraseña = contraseña.lower()
if variable == contraseña:
    print("La contraseña coincide con la guardada en la variable")
else:
    print("La contraseña no coincide con la guardada en la variable")
input("Pulsa enter para salir")