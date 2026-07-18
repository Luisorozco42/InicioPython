print("*** Calculadora en Python ***")

salir = False
while not salir:
    print("""
    Operaciones que puedes realizar:
    1. Suma
    2. Resta
    3. Multiplicación
    4. División
    5. Salir
    """)

    operacion = int(input("Escoge una operacion: "))
    
    if operacion == 1:
        valor1 = float(input("Dame el valor 1: "))
        valor2 = float(input("Dame el valor 2: "))
        print(f"El resultado de la suma es: {valor1 + valor2}")
    elif operacion == 2:
        valor1 = float(input("Dame el valor 1: "))
        valor2 = float(input("Dame el valor 2: "))
        print(f"El resultado de la resta es: {valor1 - valor2}")
    elif operacion == 3:
        valor1 = float(input("Dame el valor 1: "))
        valor2 = float(input("Dame el valor 2: "))
        print(f"El resultado de la multiplicación es: {valor1 * valor2}")
    elif operacion == 4:
        valor1 = float(input("Dame el valor 1: "))
        valor2 = float(input("Dame el valor 2: "))

        if valor2 == 0:
            print("División inválida, no se puede dividir entre 0")
        else:
            print(f"El resultado de la división es: {valor1 / valor2}")
    elif operacion == 5:
        print("Saliendo del programa de calculadora. Hasta pronto!")
        salir = True
    else:
        print("Opción no valida. Ingrese una opción válida")
