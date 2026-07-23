print("*** Repeticion de un Mensaje ***")

mensaje = input("Proporciona un mensaje a repetir: ")
numero_repeticiones = int(input("Proporciona el número de repeticiones: "))

#Iterar sobre el número de repeticiones
for i in range(numero_repeticiones): # si no se usa el valor de i se puede ubicar un "_" para demostrar que no se utilizara
    print(f"{i + 1} - {mensaje}")
