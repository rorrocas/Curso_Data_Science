from get_module import get_info
import random
import data as d

def get_base_pokemon(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name}"
    data = get_info(url)
    base_info ={
        "name": data["name"],
        "id": data["id"],
        "picture": data["sprites"]["other"]["official-artwork"]["front_default"],
        "stats": [[i["stat"],i["base_stat"]] for i in data["stats"]],
        "types": [i["type"] for i in data["types"]]
    }
    return base_info

if __name__ == "__main__":
    name = "pikachu"
    print(get_base_pokemon(name))
