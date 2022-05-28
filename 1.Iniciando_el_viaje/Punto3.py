'''Programa que convierte grados Fahrenheit a grados Centigrados o viceversa'''

option = input("Choose an option:\n1. Fahrenheit -> Centigrados\n2. Centigrados -> Fahrenheit\n")

if option=="1" or option=="2":
    value = float(input("Enter the value: "))  # pido el valor que quiere convertir y lo paso a un numero float
    if option=="1":
        print(f"{value}°F = {((value-32)*(5/9)):.2f}°C") ## Realizo conversión y lo muestro en pantalla con 2 decimales
    else:
        print(f"{value}°C = {((value*9/5)+32):.2f}°C") ## Realizo conversion y la muestro en pantalla con 2 decimales
else:
    print("Invalid option")
    