print('*** Operadores de Asignación Compuestos ***')
a,b = 10, 15
print(f"Valor inicial: {a}, b: {b}")

#operador compuesto
a += b
print(f"Operador a += b: {a}")

# operador compuesto de resta -=
a = 10
a -= b
print(f"Operador a -= b: {a}")

# Operador compuesto de multiplicación *=
a = 10
a *= b
print(f"Operador a *= b: {a}")

# Operador compuesto de division /=
a = 10 # Recordemos que esto reasigna el valor como el de un contador así que toca asignarle 10 siempre
a /= b
print(f"Operador a /= b: {a}")
