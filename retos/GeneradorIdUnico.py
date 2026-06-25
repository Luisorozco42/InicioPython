# Generador de ids unicos
from random import randint

print("*** Sistema de Generador de ID Único ***")
nombre = input("¿Cúal es tu nombre?\t")
apellido = input("¿Cúal es tu aqpellido?\t")
anio_nacimiento = input("¿Cúal es tu año de nacimiento?\t")
valor_aleatorio = randint(1, 9999)

id_unico = nombre[:2].upper() + apellido[:2].upper() + anio_nacimiento[2:] + str(valor_aleatorio)

print(f"Resultado ID único: {id_unico}")
