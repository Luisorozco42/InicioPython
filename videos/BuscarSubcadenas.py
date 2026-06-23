# Dato importante con el método find solo encontramos el inicio de la subcadena
cadena = "Hola Mundo! Mundo Mundo" # a pesar de que tenga mas de una vez la misma palabra este devolverá 6
indice = cadena.find("Mundo")
print(f"Indice de la subcadena: {indice}")

indice = cadena.find("Hola") # cabe a destacar que si no es exactamente igual devolverá -1
print(f"Indice de la subcadena de Hola: {indice}")
