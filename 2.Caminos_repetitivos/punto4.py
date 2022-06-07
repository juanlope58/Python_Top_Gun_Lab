## Punto 4, cantidad de personas de cada generación
# Por: Juan Carlos Lopera Alvarez

generacion = int(input("Ingrese la generación: ")) # Pido la generación que quiere consultar

for i in range(generacion + 1): # aumento 1 a la generación para que el bucle me pueda tomar el último valor
    print(f"Generación {i} --> {2**i} personas.") # Imprimo para cada iteración el número de personas de la generación
else:
    print("Hasta pronto!")