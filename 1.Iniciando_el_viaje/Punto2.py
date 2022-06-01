'''Programa que recibe datos personales de 3 usuarios y los muestra por pantalla'''

data=[]
data.append(input("Hello, User 1, What's your full name?"))
data.append(input("What'a your ocupation?"))
data.append(input("How old are you?"))
data.append(input("What's your city?"))
data.append(input("What's your phone number?"))
data.append(input("What is your e-mail?"))
data_users_tuple = tuple(data)      ## Guardo los datos del usuario 1 en una estructura inmutable

data=[]
data.append(input("Hello, User 2, What's your full name?"))
data.append(input("What'a your ocupation?"))
data.append(input("How old are you?"))
data.append(input("What's your city?"))
data.append(input("What's your phone number?"))
data.append(input("What is your e-mail?"))
data_users_tuple += tuple(data)     ## concateno los datos del usuario 2 en la tupla

data=[]
data.append(input("Hello, User 3, What's your full name?"))
data.append(input("What'a your ocupation?"))
data.append(input("How old are you?"))
data.append(input("What's your city?"))
data.append(input("What's your phone number?"))
data.append(input("What is your e-mail?"))
data_users_tuple += tuple(data)     ## concateno los datos del usuario 3 en la tupla
    
data_user_list = list(data_users_tuple)  # Paso los datos a una lista para mostrarlos por pantalla como se pide.

print(f"User 1: {data_user_list[:6]}\nUser 2: {data_user_list[6:12]}\nUser 3: {data_user_list[12:18]}") 
    
