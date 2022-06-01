'''Programa que convierte grados Fahrenheit a grados Centigrados'''

#Pido que me ingrese el valor a convertir y lo convierto a float
grados = float(input("Ingrese el valor que desea convertir: ")) 

## Realizo conversión  en ambos sentidos y lo muestro en pantalla con 2 decimales
print(f"{grados}°F = {((grados-32)*(5/9)):.2f}°C") 
print(f"{grados}°C = {((grados*9/5)+32):.2f}°C")