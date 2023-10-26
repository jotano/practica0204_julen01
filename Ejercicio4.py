edad = int(input("¿Cuantos años tienes?"))
ingresos = float(input("Introduce tus ingresos mensuales (€):"))
if edad > 16 and ingresos >= 1000:
    print("Tienes que tributar.")
else:
    print("No tienes que tributar.")
input("Pulsa enter para salir")