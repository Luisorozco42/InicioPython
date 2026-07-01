# Sistema para entrar o no a la casa de los espejos
print("*** Bienvenido a la casa de los espejos ***")

edad = int(input("Cual es tu edad?\n"))
miedo = input("Tienes miedo (Si/No)?\n")
tiene_miedo = miedo.strip().lower() == "si"

if not tiene_miedo and edad >= 10:
    print("Puedes entrar a la casa de los Espejos")
else:
    print("Lo siento, la Casa de los espejos podría darte miedo")
