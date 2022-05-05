from string import Template
import data as d
from get_base_info import get_base_pokemon
from get_module import get_info

template_tipos = Template("<span class='label $name'>$nombre</span>")

def build_html(base_info, doc_template = d.document_template, card_template = d.single_card):
    stats = ""
    for i in base_info["stats"]:
        stats += f"<td><h5>{get_info(i[0]['url'])['names'][4]['name']}: {i[1]}</h5></td>\n"
    tipos = ""
    for i in base_info["types"]:
        tipos += template_tipos.substitute(name = i["name"], nombre = get_info(i['url'])['names'][5]['name'])
    super_ef = ""
    for i in base_info["super_ef"]:
        super_ef += template_tipos.substitute(name = i["name"], nombre = get_info(i['url'])['names'][5]['name'])
    debil = ""
    for i in base_info["debil"]:
        debil += template_tipos.substitute(name = i["name"], nombre = get_info(i['url'])['names'][5]['name'])
    resistente = ""
    for i in base_info["resistente"]:
        resistente += template_tipos.substitute(name = i["name"], nombre = get_info(i['url'])['names'][5]['name'])
    poco_ef = ""
    for i in base_info["poco_ef"]:
        poco_ef += template_tipos.substitute(name = i["name"], nombre = get_info(i['url'])['names'][5]['name'])
    inmune = ""
    for i in base_info["inmune"]:
        inmune += template_tipos.substitute(name = i["name"], nombre = get_info(i['url'])['names'][5]['name'])
    ineficaz = ""
    for i in base_info["ineficaz"]:
        ineficaz += template_tipos.substitute(name = i["name"], nombre = get_info(i['url'])['names'][5]['name'])
    tipo_especial = ""
    for i in base_info["type_special"]:
        tipo_especial += f" <span class='label other'>{i}</span>\n"
    etapa_previa = "lorem ipsu"
    card = card_template.substitute(id = base_info["id"],
                                  name = base_info["name"].title() if  base_info["name"]!= "type-null" else "Codigo-cero",
                                  url =  base_info["picture"],
                                  tipos = tipos,
                                  description = base_info["description"],
                                  stats = stats,
                                  super_ef = super_ef,
                                  debil = debil,
                                  resistente = resistente,
                                  poco_ef = poco_ef,
                                  inmune = inmune,
                                  ineficaz = ineficaz,
                                  tipo_especial = tipo_especial,
                                  etapa_previa = etapa_previa)
    return doc_template.substitute(body=card)

if __name__ == "__main__":
    print(build_html(get_base_pokemon("pikachu")))
