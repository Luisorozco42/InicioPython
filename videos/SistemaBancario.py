# Ejemplo de sentencias de decision y el operador not para aplicar logica inversa
print("*** Bienvenido al sistema Bancario ***")
salir_sistema_txt = input('Deseas salir del sistema (Si/No)')
salir_sistema = salir_sistema_txt.strip().lower() == "si"
if not salir_sistema:
    print("Continuamos dentro del sistema")
else:
    print("Salimos del sistema")
