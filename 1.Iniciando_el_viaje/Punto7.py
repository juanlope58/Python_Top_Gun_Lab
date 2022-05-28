text = "thor lanzó su martillo#flash ha fallado por un pie! -gritó Loki Laufeyson#dos pies -le corrigió Hulk#flash menea la cabeza como disgustado… -agrega el comentarista"

lines = text.split("#") ## Separo el texto en los renglones que debe tener


for i in range(len(lines)):
    if i==0:
        lines[i] = lines[i].capitalize()+"...\n\n"  # vuelmayúscula la primera letra y le agrego los puntos al final
        
    elif i==1:
        lines[i] = lines[i].split()                 ## Esta es una forma de volver mayúscula la primera 
        lines[i][0] = lines[i][0].capitalize()      ## letra sin que se vulevan minúsculas las letras del 
        lines[i] = "¡" +" ".join(lines[i])+".\n"    ## nombre de Loki Laufeyson
        
    elif i==2:
        lines[i]= lines[i].capitalize().replace("-","").replace("hulk","Hulk")+".\n" # Esta es otra forma de volver
                                                                                     # a poner la letra de Hulk mayúscula
                                                                                     # perdida por el capitalize()               
    else:
        lines[i]=lines[i].capitalize()+".\n"
    

text_modificado= "-  ".join(lines) ## uno de nuevo la lista con todo el texto modificado
print("\n"+text_modificado)