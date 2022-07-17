from fastapi import FastAPI, HTTPException, status
from todo_api.database import Base, engine, ToDo
from pydantic import BaseModel
from sqlalchemy.orm import Session

app = FastAPI()

#create the database
Base.metadata.create_all(engine)

# create read update delete
@app.get("/")
def root():
    return "todo"

class ToDoRequest(BaseModel):
    task: str
    

# create
@app.post("/todo")
def create_todo(todo: ToDoRequest):
    #create database session
    session = Session(bind = engine, expire_on_commit=False)

    #create instance of ToDo database model
    tododb = ToDo(task = todo.task)
    
    session.add(tododb)
    session.commit()
    
    #getting the created task id
    id = tododb.id
    
    session.close()
    
    return f"created ToDo item with id {id} and description: {todo.task}"
    
#read
@app.get("/todo/{id}")
def read_todo(id: int):
    
    #
    session = Session(bind=engine,expire_on_commit=False)
    
    todo = session.query(ToDo).get(id) # SELECT * FROM todo where ID = id
    
    session.close()
    
    if not todo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"todo item {id} not found")
    
    return {"id":todo.id, "task":todo.task}

#update
@app.put("/todo/{id}")
def update_todo(id: int, task: str):
    session = Session(bind=engine,expire_on_commit=False)
    
    todo = session.query(ToDo).get(id)
    
    if todo:
        todo.task = task
        session.commit()
    
    session.close()
    
    if not todo:
        raise HTTPException(status_code=404, detail=f"todo item with id: {id}, not found")
    
    return todo

#delete
@app.delete("/todo/{id}")
def delete_todo(id: int):
    
    session = Session(bind=engine, expire_on_commit=False)
    
    todo = session.query(ToDo).get(id)
    
    if todo:
        session.delete(todo)
        session.commit()
        
    session.close()
    
    if not todo:
        raise HTTPException(status_code=404 , detail=f"todo item with id: {id}, not found ")
    return {
        "id":todo.id,
        "task":todo.task
    }

#get all
@app.get("/todo")
def read_todo_list():
    session = Session(bind=engine,expire_on_commit=False)
    
    todo_list = session.query(ToDo).all() # SELECT * FROM todo where ID = id
    
    session.close()
    
    return todo_list
