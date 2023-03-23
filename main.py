from dotenv import load_dotenv

load_dotenv()
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import uvicorn
import os

from src.define import LabelArgs, IS_DEBUG
from src.worker import Worker


# Initialize the app
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

worker = Worker()


# API
@app.post("/api/print")
async def print(data: List[LabelArgs]):
    worker.add(data)
    return "OK"


if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        host="0.0.0.0",
        port=int(os.getenv("PORT", 5000)),
        reload=IS_DEBUG,
    )
