print("*** Sistema de administración de cuentas ***")

salir = False
while not salir:
    print(f"""
    1. Crear cuenta
    2. Eliminar cuenta
    3. Salir
    """)

    opcion = int(input("Ingrese escoge una opcion: "))
    if opcion == 1:
        print("Creando tu cuenta...\n")
    elif opcion == 2:
        print("Eliminando tu cuenta...\n")
    elif opcion == 3:
        print("Saliendo del sistema. Hasta pronto!\n")
        salir = True
    else:
        print("Opción no valida, proporciona otra opción")
else: #Esto es nuevo, en python se puede usar un else para los ciclos while
    print("Terminando el sistema de Administración de Cuentas")
