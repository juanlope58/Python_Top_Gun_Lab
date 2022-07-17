from fastapi import FastAPI
from typing import Union

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello":"World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/num_primo/{numero}")
def read_num(numero: int):
    return { "primos" : primos(numero)}

def primos(numero):
    primos=[]
    if numero==1:
        primos.append(1)
    else:
        primos.append(1)
        for i in range(2,numero+1):
            cont=0
            for j in range(1,i+1):
                if (i%j)==0:
                    cont += 1
                else:
                    pass
            if cont<=2:
                primos.append(i)
            else:
                pass
    return primos