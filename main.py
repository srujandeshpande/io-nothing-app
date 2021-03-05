from fastapi import FastAPI, Form
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

origins = ["*"]  # Allow everything

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Name(BaseModel):
    person_name: str
    age: int


@app.get("/")  # root
def basic():
    return "Hello world!"


@app.get("/date")  # route
def return_date():
    res = {"date": "today"}
    return res


@app.post("/name")
def name(name_var: Name):
    name_encoded = jsonable_encoder(name_var)
    pname = name_encoded["person_name"]
    with open("names.txt", "a") as f:
        f.write(pname)
    age = name_encoded["age"]
    print(age)
    print(type(age))
    return {"status":"Welcome "+pname}


@app.get("/products")
def all_products():
    prod = [{"name": "Handbag", "price": 15}, {"name": "Handbag", "price": 15}]


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000)
