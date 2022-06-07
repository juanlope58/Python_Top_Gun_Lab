## Punto1, Capitan Luffy

# por: Juan Carlos Lopera Alvarez

# Creo las listas de criaturas y direcciones que existen.
criaturas = ["Kraken","Sirenas","Ballena","Hipocampo","Macaraprono","Pulpo","Levitantes","Hidras"]
direcciones= ["Babor", "Estribor", "Proa", "Popa"]

while (True): ## Creo un bucle con una condición que siempre se cumple hasta que encuentre un break
    criatura = input("Ingrese la criatura: ")
    
    if criatura== "stop":
        print("Misión cumplida, Adios")
        break       # Salgo del bucle si la palabra ingresada es "stop"
    elif (criatura in criaturas): # Compruebo si la criatura ingresada coincide con alguna de la lista    
        if criatura.endswith("as"): # Creo condicionales para agregar los artículos que anteceden el nombre de cada criatura
            articulo = "unas"
        elif criatura.endswith("no") or criatura.endswith("a"):
            articulo = "una"
        elif criatura.endswith("es"):
            articulo = "unos"
        else:
            articulo = "un"
    else: 
        print("Criatura desconocida.")
        continue # si ingresa una criatura inexistente vuelve al comienzo a pedir el nombre de otra criatura.
    
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