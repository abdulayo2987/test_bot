import asyncio
from TikTokApi import TikTokApi


async def fetch_video():
    async with TikTokApi() as api:
        await api.create_sessions(ms_tokens=["59uQZF5Epfi19zATnHdLuNKFFCPvXDxp44ZMx6JJtUjMhgjN2E0LZWnGQ5FAY0hPETL3QVXaPCjAs5OGRv8yWjgKg12H00zWJFvlhq326npXffjgSEumVxZ4kbGk_oeSHcUKIfX10j5LNGUPp-Yhbvx6"], num_sessions=1, sleep_after=3, headless=False, browser='webkit')
        user = api.user(username="r.boysz")

        async for video in user.videos():
            print(video.url)


asyncio.run(fetch_video())
