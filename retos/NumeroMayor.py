print("*** Bienvenido al Sistema del Mayor de 2 Números ***")

numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))
numero_mayor = numero1 if numero1 > numero2 else numero2
print(f"El número mayor es: {numero_mayor}")
