from string import Template
import data as d
from get_evo import get_evolution
from get_module import get_info

def build_evo_html(base_info, doc_template = d.document_template, evo_template = d.evo_template):
    card = ""
    nivel = 0
    for i in base_info:
        print(i)
        tipos = ""
        for j in i["types"]:
            tipos += f" <span class='label {j['name']}'>{get_info(j['url'])['names'][5]['name']}</span>\n"
        tipo_especial= ""
        for j in i["type_special"]:
            tipo_especial += f" <span class='label other'>{j}</span>\n"
        
        card_template = evo_template.substitute(nivel=f"Nivel {i['nivel']}" if i["nivel"]!=nivel else " ",
                                    id=i["id"],
                                    name=i["name"].title() if i["name"] != "type-null" else "Codigo-cero",
                                    url=i["url"],
                                    tipos=tipos,
                                    tipo_especial=tipo_especial)
        card += card_template
        nivel = i["nivel"]

    return doc_template.substitute(body=card)

if __name__ == "__main__":
    print(build_evo_html(get_evolution("pikachu")))
