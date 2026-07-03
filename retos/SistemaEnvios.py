print("*** Bienvenido al sistema de envios ***")

COSTO_NACIONAL = 10.00
COSTO_INTERNACIONAL = 20.00

peso = float(input("Introduzca el peso del paquete a enviar (kg): "))
nacional = input("Su paquete es de envio nacional o internacional? ")
es_nacional = nacional.strip().lower() == "nacional"
costo_total = 0.00

if es_nacional:
    costo_total = COSTO_NACIONAL * peso
else:
    costo_total = COSTO_INTERNACIONAL * peso

print(f"El costo de envio del paquete es de: ${costo_total:.2f}")
