# Hay que solicitar un val dentro de 0 y 5 y hay 2 constantes siendo minimo = 0 y máximo = 2
# y se debe comprobar que este valor este dentro del rango de las constantes
VALOR_MINIMO = 0
VALOR_MAXIMO = 2

print("*** Sistema Valor Dentro del Rango ***")
valor = int(input("Ingrese un valor entre 0 y 5: "))
esta_dentro_rango = VALOR_MINIMO <= valor <= VALOR_MAXIMO

print(f"Valor dentro rango: {esta_dentro_rango}")
