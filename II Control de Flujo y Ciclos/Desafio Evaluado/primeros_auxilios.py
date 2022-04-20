#Rodrigo

respuesta = input("\nPrimeros Auxilios\nLa persona que requieres primeros auxilios, ¿responde a estimulos? eliga una opcion:\n1)La persona SI responde a estimulos \n2)la persona NO responde a estimulos\nRespuesta:")
lista_si = ["1","si","Si","sI","SI"]
lista_no = ["2","no","No","nO","NO"]
if respuesta in lista_si:
	print("Evaluee la situacion y si esto amerita llevar a la persona afecta al hospital.\n")
else:
    respuesta = input("\n***Abra via Aerea***\n¿La persona respira? eliga una opcion:\n1)La persona respira\n2)La persona NO esta respirando\nRespuesta:")
    if respuesta in lista_si:
        print("\nCree un area comoda y espaciado donde la persona pueda respirar sin dificultad.")
    else:
        ambulancia = False
        print("***Administre Ventilacion y llame una ambulancia***.")
        while not(ambulancia):
            respuesta = input("\n¿La persona muestra signos de vida?\n1)La persona SI muestra signos de vida\n2)La persona NO muestra signos de vida\nRespuesta:")
            if respuesta in lista_si:
                print("\nEvaluee la situacion y si lo amerita siga esperando la ambulancia.")
                respuesta = input("\n¿La ambulancia ah llegado?\n1)La ambulancia a llegado\n2)La ambulancia aun NO llega\nRespuesta:")
                if respuesta in lista_si:
                    ambulancia = True
            else:
                respuesta = input("\n***Administre Compresion Toracica*** hasta que llegue la ambulancia.\n¿La ambulancia ah llegado?\n1)La ambulancia a llegado\n2)La ambulancia aun NO llega\nRespuesta:")
                if respuesta in lista_si:
                    ambulancia = True
        print("\nLa ambulancia a llegado")
            
        
    
