# Concepto de Truthy y Falsy (hay que saberlos para entender mejor la funcion bool)
# primeramente la función bool es para determinar que si existe o no un dato (Creo que ya se a que se refiere)
# Este solo devuelve un boolean
# Falsy, este es la representación del vacío o nada siendo los casos de 0, "", [], None
# Caso contrario Truthy, este es la representación de la existencia de algo, en otras palabras hay valores

# 1 Numeros (int, float)
print(bool(0))
print(bool(0.0))
print(bool(42))

# 2 Texto (strings)
print(bool(""))

# Cadena con espacio o texto = Algo = True
print(bool(" ")) # Esto es True
print(bool("Hola"))

# 3 None (Ausencia)
vacio = None
print(bool(vacio)) #false

print(bool(False))
print(bool(True))
