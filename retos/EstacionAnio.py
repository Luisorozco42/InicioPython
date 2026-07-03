print("*** Sistema de Estaciones del Año ***")
mes = int(input("Introduce el numero de mes: "))
estacion = ""

if (1 <= mes < 3) or mes == 12:
    estacion = "invierno"
elif 3 <= mes < 6:
    estacion = "primavera"
elif 6 <= mes < 9:
    estacion = "verano"
elif 9 <= mes < 11:
    estacion = "otoño"
else:
    print(f"El valor {mes} no es numero dentro del rango de los meses del año")

print(f"El mes {mes} tiene la estacion: {estacion}")
