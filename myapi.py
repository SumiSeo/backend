from fastapi import FastAPI, Path
from typing import Optional

app = FastAPI()

# endpoint
# localhost/delete-user
# localhost/create-user
# GET 

students = { 
    1: {
        "name" : "john",
        "age" : 17,
        "class":"year 12"
    },
    2: {
        "name" : "sam",
        "age" : 16,
        "class":"year 11"
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
    

# do not define with query parameter
@app.get("/get-by-name/{student_id}")
def get_student(*, student_id:int, name: Optional[str] = None, test:int): #If I None, meaning, it is not required 
    if students[student_id]["name"] == name:
        return students[student_id]
    return {"Data": "Not Found"}
# POST
# PUT
# DELETE




