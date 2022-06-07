# Punto 3, Leyes de la caida libre de Galileo.
# Por: Juan Carlos Lopera Alvarez

altura = float(input("ingrese la altura del edificio: "))
tiempo = 0
vel_in = 0
distancia = 0 

while(distancia < altura):      
    distancia = (vel_in*tiempo)+((9.8/2)*tiempo**2)     #formula para hallar la distancia en un tiempo determinado
    if distancia < altura:
        print(f"En el tiempo: {tiempo} s --> recorrido: {distancia:.2f} m ")
    else:
        print("Ya tocó el suelo")
    tiempo+=1
    
    