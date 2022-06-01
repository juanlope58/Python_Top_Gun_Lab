'''La siguiente matriz (o lista con listas anidadas) debe cumplir que el cuarto elemento de cada fila 
sea la suma de los tres primeros elementos de la fila respectiva. Si nota las sumas que se encuentran 
están erróneas, debe modificarlas dando 2 soluciones, una con append y otra con slicing.'''

matriz = [ [2, 4, 3], [8, 3, 4], [7, 1, 3], [9, 2, 1] ]

# Utilizando append para agregar a cada sublista un elemento con la suma de sus elementos anteriores
matriz[0].append(matriz[0][0]+matriz[0][1]+matriz[0][2])
matriz[1].append(matriz[1][0]+matriz[1][1]+matriz[1][2])
matriz[2].append(matriz[2][0]+matriz[2][1]+matriz[2][2])
matriz[3].append(matriz[3][0]+matriz[3][1]+matriz[3][2])
print(matriz)

matriz = [ [2, 4, 3, 6], [8, 3, 4, 5], [7, 1, 3, 10], [9, 2, 1, 4] ] ## Matriz erronea
matriz[0][3] = sum(matriz[0][0:3])
matriz[1][3] = sum(matriz[1][0:3])
matriz[2][3] = sum(matriz[2][0:3])
matriz[3][3] = sum(matriz[3][0:3])
print(matriz)