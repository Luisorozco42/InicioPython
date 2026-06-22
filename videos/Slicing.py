# Esto se refiere a que se puede extraer pedazos de una cadena
# Bueno ahora toca aplicar el concepto de slicing

texto = "PROGRAMACION"

# Esta es la version básica [inicio:fin]
print(texto[0:4]) # el índice 4 no va a ser recuperado

# Esta es la version para atajo del inicio de inicio a fin [:fin]
print(texto[:4])

# Esta busca desde un inicio, pero no hay que dar el final [inicio:]
print(texto[4:])

# usando índices negativos
print(texto[-4:])  # esto significa que queremos los últimos 4

# También se puede invertir la cadena
# [::-1] el inicio vacío y el final vacío, implican que va a ir de inicio a fin, pero el 3.er parametro
# indica que será de adelante hacia atrás
print(texto[::-1])

# Técnicamente, es el anterior explicado mejor
# [:: pasos] el apartado de pasos indica la dirección y cuantas letras se saltará
print(texto[::2])
