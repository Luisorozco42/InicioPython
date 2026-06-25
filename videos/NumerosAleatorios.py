# Vamos a aprender sobre los números aleatorios usando randint()
from random import randint # en caso de no especificar se necesitaría usar random.randint()

# Generar un número aleatorio entre 1 y 10
numero = randint(1, 10) # El valor a no puede ser mayor que el valor b
print(f"Numero aleatorio entre 1 y 10: {numero}")

#Simulamos un dado de 6 caras
dado = randint(1, 6)
print(f"Resultado de lanzar el dado: {dado}")
