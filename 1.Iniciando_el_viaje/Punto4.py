number_1 = 10 
number_2 = 20 
number_3 = 6.5 
 
media = (number_1 + number_2 + number_3) / 3 ## El error estaba en la prioridad de los operadores,
                                             ## Primero realiza la división y luego la suma, pero poniendo los 
                                             ## parentesis se ejecuta primero lo de adentro de ellos y luego la división
 
print(f"{media} es la nota media.")