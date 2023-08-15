from aiohttp import ClientSession

from utils.constants import BASE_URL


class HTTPSession:
    def __init__(self):
        self._session = ClientSession(base_url=BASE_URL)

    async def close_session(self):
        await self._session.close()

    @property
    def session(self):
        return self._session
