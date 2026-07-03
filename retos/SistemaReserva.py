# Técnicamente, es el mismo reto pero más complejo

print("*** Bienvenido al Sistema de Reservas del Hotel (Inserte nombre del hotel) ***")

CUARTO_TARIFA = 150.50
CUARTO_CON_VISTA_MAR_TARIFA = 190.50

nombre_cliente = input("Nombre del cliente: ")
dias_estadia = int(input("Días de estadía: "))
cuarto_vista_mar = input("Con vista al mar (Si/No)?")
tiene_vista_mar = cuarto_vista_mar.strip().lower() == "si"
costo_total = 0

if tiene_vista_mar:
     costo_total = CUARTO_CON_VISTA_MAR_TARIFA * dias_estadia
else:
    costo_total = CUARTO_TARIFA * dias_estadia

print(f"""
    Cliente: {nombre_cliente}
    Días de estadía: {dias_estadia}
    Costo Total: {costo_total}
    Habitación con vista al mar: {cuarto_vista_mar}
    """)
