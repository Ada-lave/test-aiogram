import aiohttp

class ApiClient:
    def __init__(self, base_url: str, token: str = None):
        self.base_url = base_url
        self.token = token

    async def _request(self, method: str, endpoint: str, **kwargs):
        url = f"{self.base_url}{endpoint}"
        headers = kwargs.pop("headers", {})
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        async with aiohttp.ClientSession() as session:
            async with session.request(method, url, headers=headers, **kwargs) as response:
                response.raise_for_status()
                return await response.json()

    async def get(self, endpoint: str, params: dict = None):
        return await self._request("GET", endpoint, params=params)

    async def post(self, endpoint: str, json: dict = None):
        return await self._request("POST", endpoint, json=json)

    async def put(self, endpoint: str, json: dict = None):
        return await self._request("PUT", endpoint, json=json)

    async def delete(self, endpoint: str):
        return await self._request("DELETE", endpoint)
