def choose_level(n_pregunta, p_level):
    
    # Construir lógica para escoger el nivel
    ##################################################
    
    if n_pregunta <= p_level:
        return "basicas"
    elif n_pregunta > p_level and n_pregunta <= p_level*2:
        return "intermedias"
    elif n_pregunta > p_level*2 and n_pregunta <= p_level*3:
        return "avanzadas"
    else:
        print("El numero ingresado no esta dentro del rango.")
    ##################################################

if __name__ == '__main__':
    # verificar resultados
    print(choose_level(2, 2)) # básicas
    print(choose_level(3, 2)) # intermedias
    print(choose_level(7, 2)) # avanzadas
    print(choose_level(4, 3)) # intermedias