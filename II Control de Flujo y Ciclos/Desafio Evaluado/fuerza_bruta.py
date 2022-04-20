#Rodrigo
from string import ascii_lowercase
import getpass

validar = True
while validar:
    password = getpass.getpass("Ingrese contraseña: ").lower()
    for i in password:
        if i in ascii_lowercase:
            validar = False
        else:
            validar = True
            print("Ingrese contraseña valida!!!")
            break

#password = "qwertyuiopasdfghjklzxcvbnm"

numero_de_intentos = 0
for i in password:
    for j in ascii_lowercase:
        if i == j:
            numero_de_intentos += ascii_lowercase.index(j)+1
print("numero de intentos:",numero_de_intentos)