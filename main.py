from fastapi import FastAPI
from settings import SECRET_KEY
import asyncio
import httpx

app = FastAPI()

url = "https://imdb-api.com/API/Usage/k_ujvg6j6a"


@app.get("/")
async def root():
    return {"message": "Welcome to my lazy_movie_picker backend!"}

# Sends a asyncronous request to imdb api and returns the response as json
async def test():
    async with httpx.AsyncClient() as client:
        r = await client.get("https://imdb-api.com/API/Usage/k_ujvg6j6a")
        r_data = r.json()
        return r_data

# Executes test() function and returns the response to our frontend
@app.get("/imdbTest")
async def idk():
    cool = await test()
    return cool