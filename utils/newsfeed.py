import logging

from utils.constants import API_KEY
from utils.httpsession import http_session

logging.basicConfig(level=logging.DEBUG)


class NewsFeed:
    def __init__(self):
        pass

    async def get_everything(self, query="top"):
        url = f"/v2/everything?q={query}&apiKey={API_KEY}"
        async with http_session.session.get(url) as response:
            try:
                response.raise_for_status()
                logging.debug(
                    f"Response status for get_everything url: {response.status}"
                )
                return await response.text()
            except Exception as e:
                logging.error(e)

    async def get_top_headlines(self, country="in"):
        url = f"/v2/top-headlines?country={country}&apiKey={API_KEY}"
        async with http_session.session.get(url) as response:
            try:
                response.raise_for_status()
                logging.debug(
                    f"Response status for get_top_headlines url: {response.status}"
                )
                return await response.text()
            except Exception as e:
                logging.error(e)
