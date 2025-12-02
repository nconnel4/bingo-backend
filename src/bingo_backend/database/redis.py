import redis.asyncio as redis

from bingo_backend.main import get_settings
settings = get_settings()

redis = redis.Redis().from_url(settings.redis_url, decode_responses=True)
