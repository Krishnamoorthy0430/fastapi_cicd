from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "message": "Hello CI/CD World 🚀",
        "environment": os.getenv("APP_ENV", "unknown")
        }
