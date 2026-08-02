from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class TodoCreate(BaseModel):
    title: str


class TodoUpdate(BaseModel):
    completed: bool


todos = []
next_id = 1


@app.get("/todos")
def list_todos():
    return todos


@app.post("/todos")
def create_todo(todo: TodoCreate):
    global next_id
    new_todo = {"id": next_id, "title": todo.title, "completed": False}
    todos.append(new_todo)
    next_id += 1
    return new_todo


@app.patch("/todos/{todo_id}")
def update_todo(todo_id: int, update: TodoUpdate):
    for t in todos:
        if t["id"] == todo_id:
            t["completed"] = update.completed
            return t
    return {"error": "not found"}


@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    global todos
    todos = [t for t in todos if t["id"] != todo_id]
    return {"ok": True}
