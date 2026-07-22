# Crear un programa que permita al usuario crear una contraseña y ser validada con cierto requisito
# El requisito es que esta sea mayor igual a 6 caracteres

print("*** Sistema de creación y validación de contraseña ***")
password = input("Ingrese una contraseña de 6 caracteres o más\n")

while password.strip() == "" or len(password.strip()) < 6:
    password = input("Por favor corrija el largo de la contraseña\n")
else:
    print("Su contraseña ha sido creada correctamente. Enhorabuena!")
