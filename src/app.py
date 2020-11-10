from aiohttp import web
import aiohttp_jinja2
import asyncio
import jinja2

router = web.RouteTableDef()

@router.get('/')
@aiohttp_jinja2.template('index.html')
async def index(req: web.Request):
    return {'test': req.remote}

@router.post('/upload')
async def upload(req: web.Request):
    post_data = await req.post()

    image = post_data.get('image')

    if image:
        image_content = image.file.read()
        print(image_content)

async def init():
    app = web.Application()  # app instance
    app.add_routes(router)  # add routes

    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('src/pages'))  # load templates/pages

    return app

web.run_app(init())
