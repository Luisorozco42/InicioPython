print("*** Bienvenido al sistema de autenticación ***")
USER = "admin"
PASSWORD = "admin"

user = input("Ingrese su usuario: ")
password = input("Ingrese su contraseña: ")

if user == USER and password == PASSWORD:
    print("Usuario y Contraseña válidos")
elif user != USER and password != PASSWORD:
    print("Usuario y contraseña inválidos")
elif user != USER:
    print("Usuario inválido")
else:
    print("Contraseña inválida")
