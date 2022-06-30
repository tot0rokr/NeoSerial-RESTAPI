from typing import Union

from fastapi import FastAPI

from event_proxy.client import EventProxyClient

evt_proxy = EventProxyClient()

app = FastAPI()

@app.get("/")
async def read_root():
    return "Neostack Gateway RESTapi"

def parsing_contents(contents):
    if 'args' in contents:
        args = contents['args']
    else:
        args = list()
    if 'kwargs' in contents:
        kwargs = contents['kwargs']
    else:
        kwargs = dict()
    return (args, kwargs)


# Direct Access to MeshAPI
@app.post("/api/{api}")
async def run_api(api: str, contents: Union[dict, None] = None):
    args, kwargs = parsing_contents(contents)
    ret = evt_proxy('api', api, *args, **kwargs)
    return ret

# Run Application
@app.post("/app/{app}")
async def run_app(app: str, contents: Union[dict, None] = None):
    args, kwargs = parsing_contents(contents)
    ret = evt_proxy('app', app, *args, **kwargs)
    return ret
