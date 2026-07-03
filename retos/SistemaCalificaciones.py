print("*** Bienvenido al Sistema de Calificaciones ***")

calificacion = int(input("Introduce la calificación (1-10): "))
calificacion_txt = ""

if 10 >= calificacion >= 9:
    calificacion_txt = "A"
elif 9 > calificacion >= 8:
    calificacion_txt = "B"
elif 8 > calificacion >= 7:
    calificacion_txt = "C"
elif 7 > calificacion >= 6:
    calificacion_txt = "D"
elif 6 > calificacion >= 0:
    calificacion_txt = "F"
else:
    print("Valor desconocido")

print(f"Usted obtuvo como calificación una calificación de: {calificacion_txt}")
