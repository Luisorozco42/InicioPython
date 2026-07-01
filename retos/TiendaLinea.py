print("*** Sistema de descuentos ***")

monto_compra = int(input("Ingrese el monto de su compra?\n"))
miembro_tienda = input("Erres miembro de la tienda (Si/N)?\n")
es_miembro = miembro_tienda.strip().lower() == "si"

if es_miembro and monto_compra > 1000:
    descuento = monto_compra * 0.10
    monto_final = monto_compra - descuento
    print(f"""
    Felicidades has obtenido un descuento del 10%
    Monto de la compra: {monto_compra}
    Monto del descuento: {descuento}
    Monto final con descuento: {monto_final}
    """)
elif es_miembro and monto_compra < 1000:
    descuento = monto_compra * 0.05
    monto_final = monto_compra - descuento
    print(f"""
    Felicidades has obtenido un descuento del 5%
    Monto de la compra: {monto_compra}
    Monto del descuento: {descuento}
    Monto final con descuento: {monto_final}
    """)
else:
    print(f"""
    No obtuviste ningún tipo de descuento
    Te invitamos a hacerte miembro de la tienda
    Monto final de la cuenta: {monto_compra} 
    """)