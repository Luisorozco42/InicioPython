# Se pide crear un generador de usando variables

nombre = " Ubaldo Acosta Soto "
empresa = " Global Mentoring "
dominio = "com.mx"

email = (nombre.lower().strip().replace(" ", ".") + "@" + empresa.lower().strip().replace(" ", "")
         + "." + dominio)

print(email)