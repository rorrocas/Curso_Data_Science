from string import Template

tipos_especiales = {"baby":"Bebé","legendary":"Legendario","mythical":"Mitico"}

validacion_pokemon ="""
     ***********************************************************
     Nota: Si el pokémon tiene espacios reemplace por '-'.       
     No coloque ningún tipo de signo de puntuación adicional.    
     Ejemplo: Mr. Mime, se debe ingresar como mr-mime o Mr-Mime. 
     ***********************************************************
     Ingrese un nombre valido: """

document_template = Template("""<!DOCTYPE html>
<html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="mystyle.css">
    </head>
<body>

$body

</body>
</html>
""")

single_card = Template("""<div class="column2">
    <div class="card">
    <h1>#$id $name</h1>
        <img src="$url" width="150" height="150">
    <div class="container">
        
        <h2>Estadísticas</h2>
        <table>
            <tr>
               $stats
            </tr>
        </table>
        <h3><b>Tipo</b></h3> 
            $tipos
            $tipo_especial
            
        <p>$description</p>
        
    <h3>Super efectivo contra:</h3>
        $super_ef
    <h3>Débil contra:</h3>
        $debil
    <h3>Resistente contra:</h3>
        $resistente
    <h3>Poco Eficaz contra</h3>
        $poco_ef
    <h3>Inmune contra:</h3>
        $inmune
    <h3>Ineficaz contra:</h3>
        $ineficaz

    </div>
    </div>
""")

evo_template = Template("""
<h1>$nivel</h1>
<div class="row">   
    <div class="column1">
    <div class="card">
    <h1>#$id $name</h1>
        <img src="$url" width="150" height="150">
    <div class="container">
        
        <h3><b>Tipo</b></h3> 
            $tipos
            $tipo_especial
    </div>
    </div>
    </div>
</div>
""")

validacion_pokemon = "Por favor ingrese un nombre valido de algun Pokemon: "
validacion_opcion = "Por favor ingrese una opcion valida: "

mensaje_opcion = """
                    Bienvenido a la Poke-App
                    ¿Que deseas conocer del mundo Pokemón?
                    
                    1. Pokedex
                    2. Cadena de Evolución
                    0. Salir
                    > """

mensaje_pokedex = """
    ***********************************************************
     Nota: Si el pokémon tiene espacios reemplace por '-'.       
     No coloque ningún tipo de signo de puntuación adicional.    
     Ejemplo: Mr. Mime, se debe ingresar como mr-mime o Mr-Mime. 
     ***********************************************************
     Ingrese el nombre de algun Pokemon: """

if __name__ == "__main__":
    pass