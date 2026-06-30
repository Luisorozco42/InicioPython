# Crear un programa para validar el usuario y contraseña proporcionados por el usuario
# Esto es con constantes asi que toca crearlas
USUARIO = "admin"
PASSWORD = "admin"

print(f"*** Sistema de Autenticación ***")
usuario = input(f"Cuál es tu usuario? ")
password = input(f"Cual es tu contraseña? ")
validacion_credenciales = (usuario == USUARIO and password == PASSWORD)

print(f"Datos correctos? {validacion_credenciales}")
