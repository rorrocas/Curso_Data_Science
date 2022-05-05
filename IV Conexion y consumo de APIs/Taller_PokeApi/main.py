from string import Template
from show import show_pics 
from poke_validation import validate

#Modulos creados
from get_base_info import get_base_pokemon
from build_pokemon_html import build_html
from get_species_info import get_species
from get_types_info import get_types
from get_evo import get_evolution
from build_evo_html import build_evo_html
import data as d

import time

while True:
    opcion = input(d.mensaje_opcion)
    opcion = int(validate(opcion,["0","1","2"], mensaje = d.validacion_opcion))

    if opcion == 1:
        pokemon = input(d.mensaje_pokedex).lower()
        pokemon = validate(pokemon)
        base_info = get_base_pokemon(pokemon)
        base_info.update(get_species(pokemon))
        base_info.update(get_types(pokemon))
        html = build_html(base_info)
        show_pics(html,"pokedex")
    elif opcion == 2:
        pokemon = input(d.mensaje_pokedex).lower()
        pokemon = validate(pokemon)
        base_info = get_evolution(pokemon)
        html = build_evo_html(base_info)
        show_pics(html,"evolution_chain")
    else:
        break