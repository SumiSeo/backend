from fastapi import FastAPI

app = FastAPI()

# endpoint
# localhost/delete-user
# localhost/create-user
# GET 
@app.get("/")
def index():
    return { "name" : "Sumi Seo" }


@app.get("/sumi")
def index():
    return { "name" : "Sum Sum" }


# POST
# PUT
# DELETE




