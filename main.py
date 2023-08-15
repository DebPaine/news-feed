import logging

from fastapi import FastAPI, status

from utils.newsfeed import NewsFeed

app = FastAPI()
logging.basicConfig(level=logging.DEBUG)


@app.get("/", status_code=status.HTTP_200_OK, summary="Fetches all the headlines")
async def headlines():
    try:
        response = await NewsFeed().get_top_headlines()
        # await http_session.close_session()
        return response
    except Exception as e:
        logging.error(e)
