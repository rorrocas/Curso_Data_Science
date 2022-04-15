#Rodrigo Castillo
# imc = w/(h**2)
import sys

kg = float(sys.argv[1])
altura = float(sys.argv[2])/100
IMC = kg/(altura**2)

print("Su IMC es {:.2f}".format(IMC))
if (IMC < 18.5):
    print("La clasificacion OMS es Bajo Peso.")
elif (IMC >= 18.5 and IMC < 25):
    print("La clasificacion OMS es Adecuado.")
elif (IMC >= 25 and IMC < 30):
    print("La clasificacion OMS es Sobrepeso.")
elif (IMC >= 30 and IMC < 35):
    print("La clasificacion OMS es Obesidad Grado I.")
elif (IMC >= 35 and IMC < 40):
    print("La clasificacion OMS es Obesidad Grado II.")
else:
    print("La clasificacion OMS es Obesidad Grado III.")
