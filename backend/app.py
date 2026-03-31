from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Request model
class RequestModel(BaseModel):
    topic: str

# Test route
@app.get("/")
def home():
    return {"message": "Backend is working ✅"}

# MAIN TEST (IMPORTANT)
@app.post("/generate")
def generate(data: RequestModel):
    return {"result": "HELLO FINAL"}