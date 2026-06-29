print("*** Sistema de Descuentos VIP ***")

NO_PRODUCTOS_DESCUENTO = 10
cantidad_productos = int(input("¿Cuántos productos compraste hoy?\n"))
tiene_membresia = input('¿Tienes la membresía de la tienda (Si/No)?\n')
es_elegible_descuento = (cantidad_productos >= NO_PRODUCTOS_DESCUENTO and tiene_membresia.lower() == 'si')

print(f"Tienes acceso al descuento VIP? {es_elegible_descuento}")
