# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from fastapi import FastAPI

app = FastAPI(title="Ubaid App",
    description="My First Attempt",
    version="0.0.1",
 #   terms_of_service="http://example.com/terms/",
 #   contact={
 #       "name": "Deadpoolio the Amazing",
 #       "url": "http://x-force.example.com/contact/",
#       "email": "dp@x-force.example.com",
 #   },
# #   license_info={
 #       "name": "Apache 2.0",
  #      "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
 #   },
    )

@app.get("/")
def index():
    return {"Data":{"name": "Ubaid"}}

@app.get("/about")
def about():
    return {"Data":{"About": "FastAPI"}}

@app.get("/blog/unpublished")
def unpublished():
    return {"Data ":{"Description ": "Unpublished Data"}}

@app.get("/blog/{id}")
def blog(id: int):
    return {"Data":{"Blog ID": id}}