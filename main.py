import asyncio

import httpx
from fastapi import FastAPI

from settings import SECRET_KEY

app = FastAPI()

TEST_URL = "https://imdb-api.com/API/Usage/{secret}".format(secret=SECRET_KEY)

BASE_API_URL = "https://imdb-api.com/API/"


@app.get("/")
async def root():
    return {"message": "Welcome to my lazy_movie_picker backend!"}

# Sends a asyncronous request to imdb api and returns the response as json


async def test():
    async with httpx.AsyncClient() as client:
        r = await client.get(TEST_URL)
        r_data = r.json()
        return r_data

# Executes test() function and returns the response to our frontend


@app.get("/imdbTest")
async def idk():
    cool = await test()
    return cool


async def dynamicSearch(url: str):
    async with httpx.AsyncClient() as client:
        r = await client.get(url)
        r_data = r.json()
        return r_data


@app.get("/searchByTitle/{title}")
async def SEARCH_BY_TITLE(title: str):
    search_string = BASE_API_URL + "SearchTitle/" + SECRET_KEY + "/" + title
    response = await dynamicSearch(url=search_string)
    return response
