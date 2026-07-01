# Por lo poco que he visto del video creo que tratara del orden de ejecución de los operadores
# El orden es el siguiente Paréntesis, exponente, unarios, División, Multiplicación, Módulo, suma, resta
# Comparación, Lógicos, asignación.
resultado = 12 / 3 + 2 * 3 - 1
print(f"Resultado: {resultado}")

resultado = 12 // (3 + 2) * 3 - 1
print(f"Nuevo resultado:  {resultado}")
