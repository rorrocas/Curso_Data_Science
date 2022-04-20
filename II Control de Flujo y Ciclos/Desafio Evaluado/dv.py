#Rodrigo

rut = input("Ingresa tu RUT sin puntos ni dígito verificador: ")

#rut="12345678"
serie = [2,3,4,5,6,7]

tur = list(reversed(list(rut)))

suma = 0
for i in range(len(tur)):
    if i>=len(serie):
        suma += int(tur[i])*serie[i-len(serie)]
    else:
        suma += int(tur[i])*serie[i]

operacion = 11 - suma%11

if operacion == 11:
    dv = 0
elif operacion == 10:
    dv = k
else:
    dv = operacion
    
print("Su dígito verificador es: ",dv)

