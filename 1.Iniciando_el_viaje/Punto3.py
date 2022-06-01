'''Realizar un programa que permita ingresar grados Fahrenheit y muestre por pantalla 
el dato en grados centígrados o pasar de grados centígrados a grados Fahrenheit'''

#Pido que me ingrese el valor a convertir y lo convierto a float
grados = float(input("Ingrese el valor que desea convertir: ")) 

## Realizo conversión  en ambos sentidos y lo muestro en pantalla con 2 decimales
print(f"{grados}°F = {((grados-32)*(5/9)):.2f}°C") 
print(f"{grados}°C = {((grados*9/5)+32):.2f}°C")