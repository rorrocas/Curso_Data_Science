#Rodrigo
from string import ascii_lowercase
import getpass

#password = getpass.getpass("Ingrese contraseña: ")

password = "qwertyuiopasdfghjklzxcvbnm"

numero_de_intentos = 0
for i in password:
    for j in ascii_lowercase:
        numero_de_intentos += 1
        if i == j:
            break
print("numero de intentos:",numero_de_intentos)