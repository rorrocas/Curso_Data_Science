import json 
import requests
from get_module import get_info
from get_base_info import get_base_pokemon

def get_types(name):
    tipos = get_base_pokemon(name)["types"]
    base_info ={
        "super_ef": [],
        "debil": [],
        "resistente": [],
        "poco_ef": [],
        "inmune": [],
        "ineficaz": []
    }
    for tipo in tipos:
        url = f"https://pokeapi.co/api/v2/type/{tipo['name']}"
        data = get_info(url)
        base_info ={
            "super_ef": base_info["super_ef"] + ([i for i in data["damage_relations"]["double_damage_to"]]),
            "debil": base_info["debil"] + [i for i in data["damage_relations"]["double_damage_from"]],
            "resistente": base_info["resistente"] + [i for i in data["damage_relations"]["half_damage_from"]],
            "poco_ef": base_info["poco_ef"] + [i for i in data["damage_relations"]["half_damage_to"]],
            "inmune": base_info["inmune"] + [i for i in data["damage_relations"]["no_damage_from"]],
            "ineficaz": base_info["ineficaz"] + [i for i in data["damage_relations"]["no_damage_to"]]
        }
    
    return base_info
    

if __name__ == "__main__":
    name = "combusken"
    print(get_types(name))