# Vamos a ver los distintos tipos de operadores lógicos
# Operador and (&& en otros lenguajes)
print(f"*** Operadores Lógicos ***")
condicion1 = False
condicion2 = True
resultado1 = condicion1 and condicion2
print(f"Resultado de {condicion1} and {condicion2} es: {resultado1}")

# Operador OR (|| en otros lenguajes)
resultado2 = condicion1 or condicion2
print(f"Resultado de {condicion1} or {condicion2} es: {resultado2}")

# Operador not (! en otros lenguajes)

resultado3 = not condicion1
print(f"Resultado not sobre {condicion1} es: {resultado3}")

# Revisar si una variable es una cadena vacía
nombre = ''
es_cadena_vacia = not nombre

print(f"\nLa variable no tiene ningún valor? {es_cadena_vacia}")

# Revisar si una variable no tiene ningún valor asignado
variable = None
es_variable_sin_valor = not variable

print(f"\nLa variable NO tiene ningún valor asignado? {es_variable_sin_valor}")
