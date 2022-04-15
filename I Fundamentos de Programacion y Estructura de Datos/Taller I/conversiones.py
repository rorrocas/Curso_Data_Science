#Rodrigo Ignacio Castillo Villegas
import sys
    
if __name__ == "__main__":
    
    conversion_pen = float(sys.argv[1])
    conversion_ARS = float(sys.argv[2])
    conversion_USD = float(sys.argv[3])
    clp =  float(sys.argv[4])
    print(f"Los {clp} pesos equivalen a: \n {conversion_pen*clp} Soles \n {conversion_ARS*clp} pesos Argentinos \n {conversion_USD*clp} Dólares")
    