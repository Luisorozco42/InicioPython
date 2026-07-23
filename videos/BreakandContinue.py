print("*** break y continue ***")

# Ejemplo con break
for numero in range(1, 10):
    if numero % 2 == 0:
        print(f"{numero}")
        break # rompe el ciclo (termina el ciclo completamente)

# Ejemplo con continue
for numero in range(1, 10):
    if numero % 2 == 1:
        continue # A diferencia del break este rompe la iteración no el ciclo
    else:
        print(f"{numero}")
