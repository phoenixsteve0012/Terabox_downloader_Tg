from aiohttp import web
from flask import Flask

routes = web.RouteTableDef()

@routes.get("/", allow_head=True)
async def root_route_handler(request):
    return web.json_response("Bots")


async def web_server():
    web_app = web.Application(client_max_size=90000000)
    web_app.add_routes(routes)
    return web_app

app = Flask(__name__)
port = int(os.environ.get('POT', 4650))

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(port=port)

