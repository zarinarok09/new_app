import aioredis

redis = aioredis.from_url("redis://redis")

async def cache_get(key: str):
    return await redis.get(key)

async def cache_set(key: str, value: str):
    await redis.set(key, value)

async def clear_cache(key: str):
    await redis.delete(key)