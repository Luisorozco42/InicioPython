# Por fin datos por consola xd
nombre = input("Proporciona tu nombre: ")
print(f"Tu nombre es: {nombre}")

# OJo cuidado con la conversion de datos
# Para valores de tipo numerico

edad = int(input("Edad: ")) # En este caso ya es posible trabajarlo como valor numerico
print(f"Tu edad es: {edad}")
print(edad + 5) # Caso para demostrar que es un número

# En el caso de que no se realize la transformation de tipos, este daria un error
# Ahora decimales

altura = float(input("Tu altura: "))

print(f"Tu altura es: {altura}")
