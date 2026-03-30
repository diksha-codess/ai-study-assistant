from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from openai import OpenAI

app = FastAPI()

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = OpenAI(api_key="YOUR_API_KEY")  # apni key yaha daalna

class RequestModel(BaseModel):
    topic: str

@app.post("/generate")
def generate(data: RequestModel):

    prompt = f"""
    Create a simple study plan for {data.topic}.
    Include:
    - 5 day plan
    - Key topics
    - 3 tips
    Keep it short.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return {"result": response.choices[0].message.content}