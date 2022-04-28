#Rodrigo Castillo

def get_multiple(diccionario, *claves):
  return {clave:diccionario[clave] for clave in claves}

if __name__ == __main__:
  diccionario = {"rtx 3060":600,"rx 6600":500,"rx 6600xt":550}
  print(get_multiple(diccionario,"rtx 3060","rx 6600"))
