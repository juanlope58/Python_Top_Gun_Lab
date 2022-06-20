'''Ace quiere ser voluntario para viajar a K-Pax, para ello la Agencia Espacial
Canadiense requiere que llene un formulario que ayude a obtener más información
de él y su familia. Tu debes ayudar a Ace creando un programa para completar la
información solicitada sin sobrescribir el archivo. Ten presente que los datos 
con * son los más importantes, si uno de esos campos no se llena, no podrá ser 
admitido, en caso de que el dato solicitado no sea importante, el programa deberá
poner “unknown”.

Por: Juan Carlos Lopera
'''

# Se abre el archivo en modo de solo lectura
in_file = open("required_data.txt",'r',encoding='utf-8')

#Otra forma de abrir un archivo dejando a un lado la preocupación de olvidar cerrarlo 
#Creo un archivo donde pondré los datos para no sobreescribir el fichero original
with open("Datos_Completados.txt",'a+', encoding='utf-8') as file_2:
    
    #Limpio el fichero por si ya tenía datos de ejecuciones anteriores
    file_2.seek(0)
    file_2.truncate()
    
    num_lineas=(len(in_file.readlines()))
    in_file.seek(0)     # Posiciona el puntero al inicio del fichero
    
    for i in range(num_lineas):
        linea = (in_file.readline())    #guardo cada nueva linea en esta variable
        print(linea)
        
        if '•' in linea:
            file_2.write(linea)    
            
        # Se asegura de que los campos obligatorios sean llenados            
        elif '*:' in linea:
            dato = input()
            while dato == '':
                print("Este campo es necesario")
                dato=input()
            file_2.write(linea[:-1]+' '+dato+'\n')  # Agregar al fichero la linea quitando el \n con el dato 
                                                    #solicitado y poniendolo al final 
                                                    
        #Si no se llenan los datos no obligatorios, se completan por defecto           
        elif ':' in linea:
            dato = input()
            if dato=='':
                dato = "unknown"
            file_2.write(linea[:-1]+' '+dato+'\n')
        else:
            file_2.write(' '+linea)  
in_file.close()       
    