'''A partir del ejercicio anterior, crea un programa para calcular la nota final de un estudiante 
universitario. Para ello, el usuario debe ingresar 3 notas y el valor porcentual de cada nota, 
realiza y devuelve la media por pantalla.'''


number_1 = float(input("ingrese la primera nota: "))
percent_1 = int(input("Qué porcentaje tiene? "))
number_2 = float(input("ingrese la segunda nota: "))
percent_2 = int(input("Qué porcentaje tiene? "))
number_3 = float(input("ingrese la tercera nota: "))
percent_3 = int(input("Qué porcentaje tiene? "))
 
media = (number_1*percent_1 + number_2*percent_2 + number_3*percent_3)/(percent_1+percent_2+percent_3)
 
print(f"{media} es la nota media.")