# Programa para saber si un numero es positivo
print("*** Revisión Valor Positivo ***")

numero = int(input('Proporcione un número'))

if numero > 0:
    print(f"Es positivo: {numero}")
elif numero < 0:
    print(f"Es negativo: {numero}")
else:
    print(f"El numero es: {numero}. Por lo tanto no es positivo ni negativo")
