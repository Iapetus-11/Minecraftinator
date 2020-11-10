import aiohttp
import asyncio

router = aiohttp.web.RouteTableDef()

@router.get('/')
async def index(req: aiohttp.web.Request):
    
