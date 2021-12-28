# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from fastapi import FastAPI

import schema

app = FastAPI(title="Ubaid App",
    description="My First Attempt",
    version="2.4.1",
    )

@app.get("/", tags=["Blogs"])
def index():
    return {"Data":{"name": "Ubaid"}}

@app.get("/about")
def about():
    return {"Data":{"About": "FastAPI"}}

@app.get("/blog/unpublished", tags=["Blogs"])
def unpublished():
    return {"Data ":{"Description ": "Unpublished Data"}}

@app.get("/blog/{id}", tags=["Blogs"])
def blog(id: int):
    return {"Data":{"Blog ID": id}}


@app.get("/user", tags=["Users"])
def create_user(request: schema.User):
    return request