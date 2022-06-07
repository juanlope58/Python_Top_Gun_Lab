## Punto1, Capitan Luffy

# por: Juan Carlos Lopera Alvarez

criaturas = ["Kraken","Sirenas","Ballena","Hipocampo","Macaraprono","Pulpo","Levitantes","Hidras"]
direcciones= ["Babor", "Estribor", "Proa", "Popa"]
while (True):
    criatura = input("Ingrese la criatura: ")
    if criatura== "stop":
        print("Misión cumplida, Adios")
        break
    elif (criatura in criaturas):
        if criatura.endswith("as"):
            articulo = "unas"
        elif criatura.endswith("no") or criatura.endswith("a"):
            articulo = "una"
        elif criatura.endswith("es"):
            articulo = "unos"
        else:
            articulo = "un"
    else: 
        print("Criatura desconocida.")
        continue
    
    direccion = input("Ingrese la dirección: ")
    if direccion == "stop":
        print("Mision cumplida, Adios")
        break
    elif (direccion in direcciones):
        if(direccion == "Babor") or (direccion == "Estribor") :
            prefijo = "a"
        else:
            prefijo = "por la"
    else:
        print("Corrígelo, esta dirección no extiste")
        continue
    
    print(f"¡Ahoy! capitán, {articulo} {criatura} {prefijo} {direccion}.")