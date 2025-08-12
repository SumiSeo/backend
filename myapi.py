from fastapi import FastAPI, Path

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
@app.get("/get-by-name")
def get_student(name: str):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data": "Not found"}
# POST
# PUT
# DELETE




