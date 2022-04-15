#Rodrigo Castillo

P = float(input("Ingrese precio de suscripción: "))
#U = float(input("Ingrese numero de usuario: "))
GT = float(input("Ingrese gasto total: "))

usuarios_normales = int (input("Ingrese numero de usuarios normales: "))
usuarios_premium = int (input("Ingrese numero de usuarios premium: "))

utilidades = (P *usuarios_normales - GT) +(P *1.5*usuarios_premium -GT)
print("Las utilidades son de: ",utilidades)