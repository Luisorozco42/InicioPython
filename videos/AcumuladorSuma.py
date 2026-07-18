print("*** Acumulador Suma ***")

MAXIMO = 5
numero = 1
acumulado = 0

while numero <= MAXIMO:
    #imprimir lo que se va a sumar
    print(f"(acumulado + numero) -> {acumulado} + { numero}")

    acumulado += numero
    numero += 1

    #Imprimir el resultado parcial
    print(f"Suma parcial acumulada: {acumulado} \n")

print(f"La suma acumulativa es de {acumulado}")
