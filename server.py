from aiohttp import web

routes = web.RouteTableDef()


@routes.get('/')
async def handler(request):
    return web.Response(text='Async server in python 3.10.6')


@routes.post('/add_lang')
async def add_lang(request):
    data = await request.post()
    lang = data.get('language')
    # Database stuff we can implement later
    return web.Response(text=f' {lang} was added to the database')


# @routes.get('/{language}')
# async def return_language(request):
#     lang = request.match_info.get('language', '')
#     other_info = request.rel_url.query.get('other', '')
#     return web.Response(text=f'''
#                             The Programming language entered was: {lang}
#                             other info: {other_info}
#                             ''')


async def initialization():
    app = web.Application()
    app.add_routes(routes)
    return app


web.run_app(initialization())
