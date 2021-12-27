# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def index():
    return {"Data":{"name": "Ubaid"}}

@app.get("/about")
def about():
    return {"Data":{"About": "FastAPI"}}