import httpx
from app.config import settings

async def post_to_service(path: str, json: dict, timeout: int = 10):
    url = settings.SERVICE_BASE_URL.rstrip("/") + path
    async with httpx.AsyncClient() as client:
        resp = await client.post(url, json=json, timeout=timeout)
        resp.raise_for_status()
        return resp.json()

async def get_from_service(path: str, params: dict = None, timeout: int = 10):
    url = settings.SERVICE_BASE_URL.rstrip("/") + path
    async with httpx.AsyncClient() as client:
        resp = await client.get(url, params=params, timeout=timeout)
        resp.raise_for_status()
        return resp.json()
