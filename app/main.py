from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="LexAI")


class Question(BaseModel):
    question: str


@app.get("/")
def home():
    return {
        "message": "Welcome to LexAI",
        "status": "Backend is running"
    }


@app.post("/ask")
def ask_lexai(data: Question):
    return {
        "question": data.question,
        "message": "LexAI received your question"
    }