print("*** Aplicación de Cajero Automático ***")

saldo = 1000.00
salir = False

while not salir:
    print("""
    Operaciones que puedes realizar:
    1. Consultar Saldo
    2. Retirar
    3. Depositar
    4. Salir
    """)

    opcion = int(input("Escoge una opción: "))

    if opcion == 1:
        print(f"Tu saldo actual es de: ${saldo}")
    elif opcion == 2:
        retiro = float(input("Ingresa el monto a retirar: "))
        if retiro > saldo:
            print(f"No cuentas con el saldo suficiente. Saldo actual de: ${saldo}")
        else:
            saldo -= retiro
            print(f"Tu nuevo saldo es de: ${saldo}")
    elif opcion == 3:
        deposito = float(input("Ingresa el monto a depositar: "))
        saldo += deposito
        print(f"Tu nuevo saldo es de: ${saldo}")
    elif opcion == 4:
        print("Saliendo del cajero automático. Hasta pronto!")
        salir = True
    else:
        print("Opción no valida. Ingrese una opción válida")
