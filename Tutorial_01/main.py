from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"messeage" : "hello world"}

@app.post("/")
async def post():
    return {"messeage" : "hello from the post route"}

@app.put("/")
async def put():
    return {"message" : "hello from the put route"}

@app.get("/users")
async def list_users():
    return {"messeage" : "list users route"}

@app.get("/users/me")
async def get_current_user():
    return {"Message" : "this is the current user"}

@app.get("/users/{user_id}")
async def get_user(user_id : str):
    return {"user_id" : user_id}

