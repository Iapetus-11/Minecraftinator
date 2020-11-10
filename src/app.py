from aiohttp import web
import aiohttp_jinja2
import blockinator
import asyncio
import jinja2
import cv2

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
        image_bytes = image.file.read()

        new_image_bytes = blockinator.generate(image_bytes, 1920, False)[1]
        print(type(new_image_bytes))

        cv2.imshow('image', blockinator.im_from_bytes(new_image_bytes))
        cv2.waitKey(0)
        cv2.destroyAllWindows()

async def init():
    app = web.Application()  # app instance
    app.add_routes(router)  # add routes

    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('src/pages'))  # load templates/pages

    return app

web.run_app(init())
