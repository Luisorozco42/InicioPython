from random import randint

NUMERO_SECRETO = randint(1, 50)

print("*** Bienvenido al juego de adivinar el número secreto ***")
intento = 0
numero_intento = int(input("Introduce un numero entre 1 y 50: "))

while numero_intento != NUMERO_SECRETO and intento < 11:
    if 1 <= numero_intento <= 50:
        intento += 1
        if numero_intento < NUMERO_SECRETO:
            print(f"El número {numero_intento} es menor que el número secreto")
        else:
            print(f"El número {numero_intento} es mayor que el número secreto")
        numero_intento = int(input("Introduce nuevamente un numero entre 1 y 50: "))
    else:
        print(f"El número no está entre 1 y 50")
        numero_intento = int(input("Introduce nuevamente un numero entre 1 y 50: "))
else:
    if numero_intento == NUMERO_SECRETO:
        print(f"Felicidades has encontrado el número secreto en {intento} intentos!")
    else:
        print(f"Lástima, no has encontrado el numero secreto. El número secreto era: {NUMERO_SECRETO}")
