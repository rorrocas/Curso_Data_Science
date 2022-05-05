import json
import requests
from get_module import get_info
import random
import data as d

def get_species(name):
    url = f"https://pokeapi.co/api/v2/pokemon-species/{name}"
    data = get_info(url)
    base_info ={
        "description": random.choice([i["flavor_text"] for i in data["flavor_text_entries"] if i["language"]["name"] == "es"]),
        "type_special": [j for i,j in d.tipos_especiales.items() if data[f"is_{i}"] == True]
    }
    return base_info

if __name__ == "__main__":
    name = "pichu"
    print(get_species(name))