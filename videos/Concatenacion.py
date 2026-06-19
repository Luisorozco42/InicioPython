# Concatenacion en python

nombre = "Lucia"
apellido = "Garcia"
nombre_completo = nombre + " " + apellido
# nombre_completo = nombre + " " + apellido Cabe a destacar que esto genera un error
print("Usando +: " + nombre_completo)

#Usando el metodo print
edad = 28
print("Usando comas: ", "Nombre: ", nombre_completo, ", Edad: ", edad)

# Usando F string

ciudad = "Barcelona"
pais = "España"
profesion = "Ingeniera"
presentacion = f"Hola, soy {nombre_completo}, tengo {edad + 1} años y soy {profesion} en {ciudad}, {pais}"
