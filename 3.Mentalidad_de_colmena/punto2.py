"""Saltando al 5, es una estrategia de codificación que cambia los números por su opuesto en el teclado

Por: Juan Carlos Lopera Álvarez
"""

def encode(message):
    #Función para codificar los números dados en un String.
    encoded_message=[]
    for i in range(len(message)):   
        if (message[i].isnumeric()):    # Comprobar si el caracter es un numero
            encoded_message.append(convert(message[i]))    # si es un número entonces se llama a otra función que hace
            continue                                       # la codificación de los números y se agrega a la lista
        else:
            encoded_message.append(message[i])     # Agrar el caracter a la lista
    return(''.join(encoded_message))    # Unir la lista para que quede en un String y retornar el mensaje codificado.
            
## especie de Switch case: hecho con if y elifs
def convert(num):
    # Funcion para convertir los números haciendo la codificación llamada saltando al 5.
    if num == '0':
        return '5'
    elif num == '1':
        return '9'
    elif num == '2':
        return '8'
    elif num == '3':
        return '7'
    elif num == '4':
        return '6'
    elif num == '5':
        return '0'
    elif num == '6':
        return '4'
    elif num == '7':
        return '3'
    elif num == '8':
        return '2'
    elif num == '9':
        return '1'
        
###########
# Como anotación, la función para codificar y decodificar es la misma.
###########

message = input("Cuál es el mensaje que quieres codificar o decodificar?")
coded_message = encode(message)
print(coded_message)