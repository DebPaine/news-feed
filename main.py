import logging

from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware

from utils.newsfeed import NewsFeed

app = FastAPI()
logging.basicConfig(level=logging.DEBUG)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get(
    "/headlines", status_code=status.HTTP_200_OK, summary="Fetches all the headlines"
)
async def headlines():
    try:
        response = await NewsFeed().get_top_headlines()
    except Exception as e:
        logging.error(e)
    else:
        return response


@app.get("/all", status_code=status.HTTP_200_OK, summary="Fetches all the news")
async def everything():
    try:
        response = await NewsFeed().get_everything()
    except Exception as e:
        logging.error(e)
    else:
        return response
