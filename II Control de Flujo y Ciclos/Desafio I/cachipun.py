import random
import sys

jugadas = ["piedra","papel","tijera"]

jugador = (sys.argv[1])
if jugador in jugadas:
    computador = random.choice(jugadas)
    print(f"Tu jugaste {jugador}\nComputador jugo {computador}. " )
    if (jugador == "piedra" and computador == "tijera") or (jugador == "papel" and computador == "piedra") or (jugador == "tijera" and computador == "papel"):
        print("Ganaste c:")
    elif jugador == computador:
        print("Empate ._.")
    else: 
        print("Perdiste :c")
        
else:
    print("Argumento inválido: Debe ser piedra, papel o tijera.")