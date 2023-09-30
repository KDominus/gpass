import g4f
import asyncio
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Question(BaseModel):
    text: str


@app.post("/gpt")
async def ask_gpt(question: Question):
    response = await g4f.ChatCompletion.create_async(
        model=g4f.models.gpt_4,
        messages=[{"role": "user", "content": question.text}],
    )

    return {"answer": response}


@app.post("/gpt_old")
async def ask_gpt(question: Question):
    response = await g4f.ChatCompletion.create_async(
        model=g4f.models.gpt_35_turbo,
        messages=[{"role": "user", "content": question.text}],
    )

    return {"answer": response}
