from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

# endpoint
# localhost/delete-user
# localhost/create-user
# GET 

students = { 
    1: {
        "name" : "john",
        "age" : 17,
        "year":"year 12"
    },
    2: {
        "name" : "sam",
        "age" : 16,
        "year":"year 11"
    }
}


@app.get("/")
def index():
    return { "name" : "Sumi Seo" }


@app.get("/sumi")
def index():
    return { "name" : "Sum Sum" }


@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(..., description="The ID of the student that you want to view.", gt=0)):
    return students[student_id]
    

# # do not define with query parameter
# @app.get("/get-by-name/{student_id}")
# def get_student(*, student_id:int, name: Optional[str] = None, test:int): #If I None, meaning, it is not required 
#     if students[student_id]["name"] == name:
#         return students[student_id]
#     return {"Data": "Not Found"}
# # POST
# # PUT
# # DELETE


class Student(BaseModel):
    name: str
    age: int
    year: int
    
    
@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"Error":"This student already exists"}
    
    students[student_id] = student
    return students[student_id]


@app.put("/update-student/{student_id}")
def update_student(student_id: int, name: str):
    for student_id in students:
        if student_id == student_id:
            students[student_id]["name"] = name
            return students[student_id]
        else:
            return {"Error":"This student id do not exist"}