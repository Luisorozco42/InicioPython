# Funciones .upper o .lower
# tenemos que tener en cuenta que las cadenas de caracteres son inmutables

animal = "Gato"

# animal[4] = "s" (Esto provoca un error)
# Lo correcto seria concatenar (+)

plural = animal + "s"

print(animal)
print(plural)

print(animal.upper())
print(animal.lower())

# Otro caso de concatenacion
plural = f"{animal}s"
print(plural)
