'''Debes utilizar todo lo que sabes sobre los strings, las listas y sus métodos o funciones 
para transformar el siguiente texto:
thor lanzó su martillo#flash ha fallado por un pie! -gritó Loki Laufeyson#dos pies -le corrigió Hulk#flash menea la cabeza como disgustado… -agrega el comentarista
En:
Thor lanzó su martillo…

- ¡Flash ha fallado por un pie! -gritó Loki Laufeyson.
- Dos pies le corrigió Hulk.
- Flash menea la cabeza como disgustado… -agrega el comentarista.'''


text = "thor lanzó su martillo#flash ha fallado por un pie! -gritó Loki Laufeyson#dos pies -le corrigió Hulk#flash menea la cabeza como disgustado… -agrega el comentarista"

lines = text.split("#") ## Separo el texto en los renglones que debe tener

lines[0] = lines[0].capitalize()+"...\n\n"  # vuelmayúscula la primera letra y le agrego los puntos al final


lines[1] = lines[1].split()                 ## Esta es una forma de volver mayúscula la primera 
lines[1][0] = lines[1][0].capitalize()      ## letra sin que se vulevan minúsculas las letras del 
lines[1] = "¡" +" ".join(lines[1])+".\n"    ## nombre de Loki Laufeyson
        

lines[2]= lines[2].capitalize().replace("-","").replace("hulk","Hulk")+".\n" # Esta es otra forma de volver
                                                                            # a poner la letra de Hulk mayúscula
                                                                            # perdida por el capitalize()               

lines[3]=lines[3].capitalize()+".\n"
    
text_modificado= "-  ".join(lines) ## uniendo de nuevo la lista con todo el texto modificado
print("\n"+text_modificado)