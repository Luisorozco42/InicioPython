#Tipos de datos

# str (string)
nombre = "Capitana python"
poderPrincipal = "Controlar los bugs con la mente"

# int (integer)
edad = 28
misionesCompletadas = 42

# float (flotantes)
nivelEnergia = 99.8

# bool (Bolean)
tieneCapa = True
esVillano = False

# None (No value)
companiaActual = None

# Mostrar la info

print("=== Ficha del super heroe ===")
print("Nombre: ", nombre)
print("Poder: ", poderPrincipal)
print("Edad: ", edad)
print("Misiones Completa: ", misionesCompletadas)
print("Nivel Energía: ", nivelEnergia)
print("Tiene Capa: ", tieneCapa)
print("Es villano: ", esVillano)
print("Compañía Actual: ", companiaActual)

# Esto funciona para saber que tipo es la variable
# Hay que saber que los tipos de datos en python pueden cambiar
#Esto lo hace un lenguaje dinámico

print(type(nombre))
print(type(tieneCapa))
print(type(companiaActual))