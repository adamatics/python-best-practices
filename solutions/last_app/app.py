import requests
from fastapi import FastAPI

app = FastAPI()

EXTERNAL_API_URL = "https://jsonplaceholder.typicode.com/posts"

@app.get("/")
def read_root():
    return {"message": "Hello, World"}

@app.get("/posts/{post_id}")
def get_post(post_id: int):
    response = requests.get(f"{EXTERNAL_API_URL}/{post_id}")
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Post not found"}, response.status_code

@app.post("/posts")
def create_post(post: dict):
    response = requests.post(EXTERNAL_API_URL, json=post)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to create post"}, response.status_code