#ROdrigo CAstillo
#V=sqr(2gr)

radio = float(input("Ingrese radio del planeta en kilometros: "))
constante = float(input("Ingrese la constante gravitacional del planeta: "))

print("La velocidad de escape es: {:.2f}[m/s]".format((2*radio*1000*constante)**(1/2)))