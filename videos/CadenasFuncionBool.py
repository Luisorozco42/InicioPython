# Esto seran ejemplos de cadenas en conjunto de la function bool
# Primeramente errores comunes

respuesta_usuario = "False" # Se le conoce como error comun debido a que suelen confundir texto con el False
# para mí es lógico que son 2 cosas distintas, pero creo que puede pasar en principiantes

# La funcion bool si el string esta vacio
es_verdad = bool(respuesta_usuario)
print(f"El valor es: {es_verdad}")

texto_vacio = ""
print(bool(texto_vacio))

