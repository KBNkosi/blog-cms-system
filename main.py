from fastapi import FastAPI
from app.api import posts

app = FastAPI()

app.include_router(posts.router)

@app.get("/")
async def root():
    return {"message": "Hello from the main app!"}