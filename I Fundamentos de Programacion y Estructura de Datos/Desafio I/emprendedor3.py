#Rodrigo Castillo

P = float(input("Ingrese precio de suscripción: "))
U = float(input("Ingrese numero de usuario: "))
GT = float(input("Ingrese gasto total: "))

utilidades_pasadas = float(input("Ingrese utilidades año pasado: "))

utilidades = 100*(P * U - GT)/utilidades_pasadas

print("el crecimiento a sido del: {:.2f}% en comparacion al año pasado.".format(utilidades)) 