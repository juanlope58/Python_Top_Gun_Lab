matriz = [ [2, 4, 3], [8, 3, 4], [7, 1, 3], [9, 2, 1] ]

# Utilizando append para agregar a cada sublista un elemento con la suma de sus elementos anteriores
for i in range(len(matriz)):
    matriz[i].append(sum(matriz[i]))
print(matriz)

matriz = [ [2, 4, 3, 6], [8, 3, 4, 5], [7, 1, 3, 10], [9, 2, 1, 4] ] ## Matriz erronea

for j in range(len(matriz)):
    matriz[j][3] = sum(matriz[j][0:3])

print(matriz)