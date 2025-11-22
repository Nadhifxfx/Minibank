from fastapi_limiter import FastAPILimiter
import aioredis
from app.config import settings

async def init_rate_limiter(app):
    redis = await aioredis.from_url(settings.REDIS_URL, encoding="utf8", decode_responses=True)
    await FastAPILimiter.init(redis)
