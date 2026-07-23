print("*** Dibujar un Triángulo Simétrico ***")

numero_filas = int(input("Ingrese el número de filas: "))

for fila in range(1, numero_filas + 1):
    espacios_blanco = " " * (numero_filas - fila)
    asteriscos = "*" * (2 * fila - 1)
    print(espacios_blanco + asteriscos + espacios_blanco)
