## Punto 2, detector de velocidad y multas.
# Por: Juan Carlos Lopera Alvarez

distancia1 = float(input("Distancia 1: "))
distancia2 = float(input("Distancia 2: "))
tiempo = float(input("Tiempo: "))
multa = False    # Bandera para saber si se obtiene una multa por alta velocidad

if tiempo != 0:  # Me aseguro que no haya división por cero
    velocidad = round((distancia1 - distancia2)/tiempo) #Convierto la velocidad a un entero
    if velocidad < 0:       # Convierto la velocidad a positiva en caso de que sea negativa
        velocidad *= -1
    else:
        pass            # Esto solo por usar la instrucción pass, pero no es necesaria
else:
    print("Error: división por cero")
    velocidad = 0
    
print(velocidad)
## Condicionales para definir el llamado de atención o multa a impartir
if 0 <= velocidad <= 20:
    print("Está conduciendo a muy baja velocidad")
    
elif 21 <= velocidad <= 60: 
    print("Velocidad normal")
     
elif 61 <= velocidad <=80 :
    print("Está conduciendo a alta velocidad")

elif 81 <= velocidad <= 120:
    multa = True
    print("Obtiene una Multa tipo 1 por alta velocidad")
    
else: 
    multa = True
    print("Obtiene una multa tipo 2 por alta velocidad y se le inmovilizará el vehículo")
    
if multa:       # Compruebo si obtubo multa de velocidad
    print("Se le realizará un examen de alcoholemia")
    resultado = int(input("Ingrese el resultado de la prueba: "))
    
    if 20 <= resultado <= 39:
        print("También se le suspende la licencia de 6 a 12 meses")
    elif 40 <= resultado <= 99:
        print("Primer grado de embriaguez: también se le suspende la licencia de 1 a 3 años") 
    elif 100 <= resultado <= 149:
        print("""Segundo grado de embriaguez: También se le suspende la licencia de 3 a 5 años,
              ademas de realizar un curso de sensibilización de mínimo 40 horas""")
    elif resultado >= 150:
        print("""Tercer grado de embriaguez: También se le suspende la licencia de 5 a 10 años,
              ademas de realizar un curso de sensibilización de mínimo 80 horas""")
    else: 
        print("No tiene más sanciones.")