# Esto es un sistema de ticket de venta
print('*** Generación Ticket de Venta ***')

precio_leche = float(input("Precio Leche: "))
precio_pan = float(input("Precio Pan: "))
precio_lechuga = float(input("Precio Lechuga: "))
precio_platanos = float(input("Precio Platanos: "))
descuento_porcentaje = int(input("Aplicar algún descuento (%)?: "))

# Cálculo del subtotal (Sin impuestos)
subtotal = precio_leche + precio_pan + precio_lechuga + precio_platanos

# Aplicar el descuento
descuento = subtotal * descuento_porcentaje/100

# Subtotal con descuento
subtotal_con_descuento = subtotal - descuento

# Cálculo co impuestos (16%)
impuesto = subtotal_con_descuento * 0.16

# Cálculo total de la compra (Con impuestos)
costo_total_compra = subtotal_con_descuento + impuesto
print(f"""
Subtotal: ${subtotal:.2f}
Descuento: ${descuento:.2f} ({descuento_porcentaje} %)
Subtotal con Descuento: ${subtotal_con_descuento:.2f}
Impuesto (16%): ${impuesto:.2f}
Costo total de la compra: ${costo_total_compra:.2f}""")
