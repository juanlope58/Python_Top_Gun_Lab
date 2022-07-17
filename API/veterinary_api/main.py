from pydantic import BaseModel
from database import Veterinary, base, engine
from fastapi import FastAPI, HTTPException
from sqlalchemy.orm import Session

app = FastAPI()

#Create the database 
base.metadata.create_all(engine)

#Create read update delete
@app.get("/")
def root():
    return "veterinary"

class VeterinaryRequest(BaseModel):
    name: str
    age: int
    race: str
    species: str
    
@app.post("/veterinary")
def createPet(pet: VeterinaryRequest):
    
    session = Session(bind=engine, expire_on_commit=False)
    
    newPet = Veterinary(
        name = pet.name,
        age = pet.age,
        race = pet.race,
        species = pet.species)
    
    session.add(newPet)
    session.commit()
    
    id = newPet.id
    session.close()
    return newPet

@app.get("/veterinary/{id}")
def getPet(id:int):
    session=Session(bind=engine, expire_on_commit=False)
    
    pet = session.query(Veterinary).get(id)
    
    session.close()
    if not pet:
        raise HTTPException(status_code=404,detail=f"the pet with id: {id}, does not exist")
    
    return pet
    
@app.put("/veterinary/{id}")
def updatePet(id:int, name:str, age:int, race:str, species:str):
    
    session= Session(bind=engine, expire_on_commit=False)
    
    pet = session.query(Veterinary).get(id)
    
    if pet:
        pet.name = name
        pet.age = age
        pet.race = race
        pet.species = species
        session.commit()   
             
    session.close()
    if not pet:
        raise HTTPException(status_code=404, detail=f"the pet with id: {id} doesn't exist")
    return pet

@app.delete("/veterinary/{id}")
def deletePet(id: int):
    
    session = Session(bind=engine, expire_on_commit=False)
    
    pet = session.query(Veterinary).get(id)
    
    if pet:
        session.delete(pet)
        session.commit()
        
    session.close()
    if not pet:
        raise HTTPException(status_code = 404, detail = f"The Pet with id: {id}, was not found")
    return pet
    
@app.get("/veterinary")
def getAll():
    
    session=Session(bind=engine, expire_on_commit=False)
    
    allPets = session.query(Veterinary).all()
    
    session.close()
    
    return allPets
