'''Programa que recibe datos personales de 3 usuarios y los muestra por pantalla'''

data_users=()
# bucle para pedir a los 3 usuarios sus datos
for i in range(3):
    data=[]
    print(f"Hello User {i+1}")
    data.append(input("What's your full name?"))
    data.append(input("What'a your ocupation?"))
    data.append(input("How old are you?"))
    data.append(input("What's your city?"))
    data.append(input("What's your phone number?"))
    data.append(input("What is your e-mail?"))
    
    data_users += tuple(data)    # guardo los datos en una colección inmutable
    
data_user_list = list(data_users)  # Paso los datos a una lista para mostrarlos por pantalla como se pide.

print(f"User 1: {data_user_list[:6]}\nUser 2: {data_user_list[6:12]}\nUser 3: {data_user_list[12:18]}") 
    
