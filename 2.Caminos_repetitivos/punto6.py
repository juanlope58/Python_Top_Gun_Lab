## Punto 6, intersección de listas.
# Por: Juan Carlos Lopera Alvarez

lista1 = ['h', 'e', 'l', 'l', 'o', ' ', 't', 'e', 'a', 'm']
lista2 = ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
lista3=[]

for i in lista1:                                # Recorro la lista1
    if (i in lista2) and (i not in lista3):     # Si el elemeto de la lista1 se repite en la lista2 y no se ha agregado
                                                # a la lista 3, entonces lo agrego.
        lista3.append(i)
            
print("La nueva lista es:",lista3)
