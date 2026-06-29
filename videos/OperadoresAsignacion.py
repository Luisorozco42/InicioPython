# Toca ver ahora los operadores de asignación
print("*** Operadores de Asignación ***")
numero = 5
print(f"Valor de numero: {numero}")
numero = 10
print(f"Valor de numero: {numero}")
cadena = 'Saludos desde Python'
print(f"Valor de cadena: {cadena}")

# Asignación múltiple
x, y, z = 5, 'Hola', -9.15
print(f"Valor de x = {x}, y = {y}, z = {z}")

# Asignación encadenada (todas las variables van a tener el mismo valor inicial)
a = b = c = 10
print(f"Valor de a = {a}, b = {b}, c = {c}")

# Intercambio de valores de una variable sin necesidad de una variable temporal
x, y = 5, 10
print(f"Valores iniciales x = {x}, y = {y}")
# Aplicación de asignación múltiple, intercambiamos valores
x, y = y, x
print(f"Valores intercambiados x = {x}, y = {y}")

# Recibir múltiples valores de la entrada del usuario
nombre, apellido = input('Ingresa tu nombre y apellido separados por una coma: ').split(',')
print(f"Nombre: {nombre.strip()}, Apellido: {apellido.strip()}")
