## Punto 5, Tablero cuadrado 
# Por: Juan Carlos Lopera Alvarez

longitud = int(input("Ingrese la longitud del tablero: "))

for i in range(longitud):
    for k in range(3):                  # Con este bucle se copia cada fila tres veces
        for j in range(longitud):
            if ((i+j)%2)!=0:            # Con esta condición se obriene la iterabilidad de los cuadros blancos con negros, comenzando con blanco
                print("* * *", end="")  # Con la intención de hacer más cuadrado el tablero, agregué espacios entre los asteriscos
            else:
                print("      ",end="")        
        print()
        j=0
    