import requests
import json
from string import Template

img_template = Template('<img src="$url">')

def request_get(url):
    return json.loads(requests.get(url).text)

out = request_get('https://jsonplaceholder.typicode.com/photos')[:5]

imagen = img_template.substitute(url = 'hola')

html_template = Template('''<!DOCTYPE html>
<html>
<head>
<title>Título de la Página</title>
</head>
<body>
<h1>Nuestra página Web</h1>
$body
</body>
</html>
''')
#print(html_template.substitute(body = imagen))

lista_url = [elemento['url'] for elemento in out]
texto_img = ''
for url in lista_url:
    texto_img += img_template.substitute(url = url)+'\n'
    #print(texto_img)
    html = html_template.substitute(body = texto_img)
print(html)
with open('output.html','w') as f:
    f.write(html)
