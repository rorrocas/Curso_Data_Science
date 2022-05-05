import json
import requests
from get_module import get_info
from get_base_info import get_base_pokemon
from get_species_info import get_species
import random
import data as d

def get_evolution(name):
    url = f"https://pokeapi.co/api/v2/pokemon-species/{name}"
    url_evo = get_info(url)["evolution_chain"]["url"]
    data = get_info(url_evo)
    #data_info = get_base_pokemon(name)
    #data_species = get_species(name)
    cadena = data["chain"]
    lista_base_info = []
    nivel = 1
    while len(cadena) != 0:
        if nivel == 1:
            data_info = get_base_pokemon(cadena["species"]["name"])
            data_species = get_species(cadena["species"]["name"])
            base_info ={
            "name": cadena["species"]["name"],
            "nivel": nivel,
            "id": data_info["id"],
            "url": data_info["picture"],
            "types": [i for i in data_info["types"]],
            "type_special": [i for i in data_species["type_special"]]
            }
            lista_base_info.append(base_info)
        else:
            for j in cadena:
                data_info = get_base_pokemon(j["species"]["name"])
                data_species = get_species(j["species"]["name"])
                base_info ={
                "name": j["species"]["name"],
                "id": data_info["id"],
                "nivel": nivel,
                "url": data_info["picture"],
                "types": [i for i in data_info["types"]],
                "type_special": [i for i in data_species["type_special"]]
                }
                lista_base_info.append(base_info)
        
        if nivel == 1:
            cadena = cadena["evolves_to"]
            nivel += 1
        else:
            if len(cadena[0]["evolves_to"]) == 0:
                break
            else:
                cadena = cadena[0]["evolves_to"]
                nivel += 1
        
    
    return lista_base_info

if __name__ == "__main__":
    name = "wurmple"
    print(get_evolution(name))

"""
        elif nivel == 3:
            for j in cadena:
                for x in range(len(j["evolves_to"])):
                    data_info = get_base_pokemon(j["evolves_to"][x]["species"]["name"])
                    data_species = get_species(j["evolves_to"][x]["species"]["name"])
                    base_info ={
                    "name": j["evolves_to"][x]["species"]["name"],
                    "id": data_info["id"],
                    "nivel": nivel,
                    "url": data_info["picture"],
                    "types": [i for i in data_info["types"]],
                    "type_special": [i for i in data_species["type_special"]]
                    }
                    lista_base_info.append(base_info)
        """