#Rodrigo
from string import ascii_lowercase
import getpass

#password = getpass.getpass("Ingrese contraseña: ")

password = "qwertyuiopasdfghjklzxcvbnm"

numero_de_intentos = 0
for i in password:
    if i in ascii_lowercase:
        numero_de_intentos += ascii_lowercase.index(i)+1
print("numero de intentos:",numero_de_intentos)