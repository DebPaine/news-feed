from aiohttp import ClientSession

from utils.constants import BASE_URL


class HTTPSession:
    def __init__(self):
        self._session = ClientSession(base_url=BASE_URL)

    async def close_session(self):
        await self._session.close()

    @property
    def session(self):
        # if self._session.closed:
        #     self._session = ClientSession(base_url=BASE_URL)
        return self._session


# HTTPSession singleton instance so that it's reused across the entire app
http_session = HTTPSession()
