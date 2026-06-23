# Aparentemente en python puedes usar el * para crear copias concatenadas una cierta cantidad de veces print("-" * 20)
# por lo tanto la formula es "Cadena" * Integer
# Si multiplicamos por 0 osea "Caedena" * 0 esto es una cadena vacia

#Primer ejemplo: Separador visual
linea = "=" * 20
print(linea)

#Segundo ejemplo: Sangria
nivel = 2
sangria = "    " * nivel
print(sangria)

# 3er ejemplo: patrones simples
print("1" * 5)

#Error comun se deja en comentario para evitar un crash
# print("Hola" * 2.5) Esto da error de tipado
